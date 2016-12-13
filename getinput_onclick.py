import Tkinter as tk

class MyApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.entry = tk.Entry(self)
        self.entry.pack()
        close_button = tk.Button(self, text="Close", command=self.close)
        close_button.pack()
        self.string = ""

    def close(self):
        global result
        self.string = self.entry.get()
        self.destroy()

    def mainloop(self):
        tk.Tk.mainloop(self)
        return self.string

print "enter a string in the GUI"
app = MyApp()
result = app.mainloop()
print "you entered:", result




from Tkinter import *

def show_entry_fields():
   print("First Name: %s\nLast Name: %s" % (e1.get(), e2.get()))

master = Tk()
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=show_entry_fields).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )
