import json

class MarkingPositionMonitor:
    def __init__(self):
        self.__message__ = {}
        self.markingPosition = {}
        self.order = {}

    def on_event(self, message):
        self.__message__ = json.loads(message)
        type = self.__message__['type']
        if type == 'NEW':
            if self.__message__['side'] == 'SELL':
                return self.newSell_event()
            elif self.__message__['side'] == 'BUY':
                return self.newBuy_event()
        elif type == 'ORDER_REJECT':
            return self.order_reject()
        elif type == 'ORDER_ACK':
            return self.order_ack()
        elif type == 'CANCEL':
            return self.cancel()
        elif type == 'CANCEL_ACK':
            return self.cancel_ack()
        elif type == 'CANCEL_REJECT':
            return self.cancel_reject()
        elif type == 'FILL':
            return self.fill()

    def newSell_event(self):
        order_id = self.__message__['order_id']
        quantity, remaining = self.__message__['quantity'], self.__message__['quantity']
        symbol = self.__message__['symbol']
        self.order[order_id] = ('SELL', quantity, symbol, remaining)
        self.markingPosition[symbol] = self.markingPosition.get(symbol, 0) - quantity

    def newBuy_event(self):
        order_id = self.__message__['order_id']
        quantity, remaining = self.__message__['quantity'], self.__message__['quantity']
        symbol = self.__message__['symbol']
        self.order[order_id] = ("BUY", quantity, symbol, remaining)
        self.markingPosition[symbol] = self.markingPosition.get(symbol, 0)
        return self.markingPosition[symbol]

    def order_ack(self):
        order_id = self.__message__['order_id']
        side, quantity, symbol, remaining = self.order[order_id]
        return self.markingPosition[symbol]

    def order_reject(self):
        order_id = self.__message__['order_id']
        side, quantity, symbol, remaining = self.order[order_id]
        if side == "SELL":
            self.markingPosition[symbol] += quantity
        self.order.pop(order_id)
        return self.markingPosition[symbol]


    def cancel(self):
        order_id = self.__message__['order_id']
        if order_id not in self.order:
            return 0
        else:
            side, quantity, symbol, remaining = self.order[order_id]
        if remaining == 0:
            return 0
        else:
            return self.markingPosition[symbol]

    def cancel_ack(self):
        order_id = self.__message__['order_id']
        if order_id not in self.order:
            return 0
        else:
            side, quantity, symbol, remaining = self.order[order_id]
            if side == "SELL":
                self.markingPosition[symbol] += remaining
            elif side == "BUY":
                self.markingPosition[symbol] -= remaining
            return self.markingPosition[symbol]

    def cancel_reject(self):
        order_id = self.__message__['order_id']
        if order_id not in self.order:
            return  0
        else:
            side, quantity, symbol, remaining = self.order[order_id]
        return self.markingPosition[symbol]

    def fill(self):
        order_id = self.__message__['order_id']
        side, quantity, symbol, remaining = self.order[order_id]
        filled_quantity = self.__message__['filled_quantity']
        remaining -= filled_quantity
        if side == "BUY":
            self.markingPosition[symbol] = self.markingPosition.get(symbol, 0) + filled_quantity
        return self.markingPosition[symbol]
