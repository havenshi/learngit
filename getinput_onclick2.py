from Tkinter import *
from test import flighttime_module as fm
class HavenButtons:
    def __init__(self,master):
        frame=Frame(master)
        frame.pack()

        self.label_ff = Label(frame, text="Enter the city and time you fly from", fg="blue")
        self.label_ft = Label(frame, text="Enter the city and time you fly to", fg="blue")
        self.label_1 = Label(frame, text="Fly from:")
        self.label_2 = Label(frame, text="Departure time:")
        self.label_3 = Label(frame, text="Fly to:")
        self.label_4 = Label(frame, text="Arrival time:")
        self.entry_1 = Entry(frame)
        self.entry_2 = Entry(frame)
        self.entry_3 = Entry(frame)
        self.entry_4 = Entry(frame)

        self.label_ff.grid(row=0, columnspan=2, sticky=W)
        self.label_1.grid(row=1, sticky=E)
        self.label_2.grid(row=2, sticky=E)
        self.entry_1.grid(row=1, column=1)
        self.entry_2.grid(row=2, column=1)

        self.label_ft.grid(row=3, columnspan=2, sticky=W)

        self.label_3.grid(row=4, sticky=E)
        self.label_4.grid(row=5, sticky=E)
        self.entry_3.grid(row=4, column=1)
        self.entry_4.grid(row=5, column=1)


        self.okButton=Button(frame,text="Ok",command=self.printMessage)
        self.okButton.pack(side=LEFT)
        self.okButton.grid(row=6, columnspan=2)

        self.quitButton=Button(frame,text="Quit",command=frame.quit)
        self.quitButton.pack(side=LEFT)
        self.quitButton.grid(row=6, column=1, columnspan=2)

    def printMessage(self):
        s=fm.flightTime()
        print s.ft(self.entry_1.get(), self.entry_2.get(), self.entry_3.get(), self.entry_4.get())

root = Tk()
b=HavenButtons(root)
root.mainloop()