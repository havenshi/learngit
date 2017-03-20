class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        sum = 0 # total remained gas
        subsum = 0 # remained gas for each period
        index = 0
        for i in range(len(gas)):
            if subsum + gas[i] - cost[i] >= 0: # can come to next station
                subsum += gas[i] - cost[i]
                sum += gas[i] - cost[i]
            else:
                subsum = 0
                index = i + 1 # recount from next station
                sum += gas[i] - cost[i] # still the total
        if sum<0:    # total gas can not cover a circle
            return -1
        else:
            return index