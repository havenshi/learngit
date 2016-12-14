from Tkinter import *
# # Lesson 1
# root = Tk()
#
# theLabel = Label(root,text="easy")
# theLabel.pack()
#
# root.mainloop()

# # Lesson 2
# root = Tk()
#
# topFrame=Frame(root)
# topFrame.pack()
# bottomFrame=Frame(root)
# bottomFrame.pack(side=BOTTOM)
#
# button1=Button(topFrame,text="button1",fg="red")
# button2=Button(topFrame,text="button2",fg="blue")
# button3=Button(topFrame,text="button3",fg="green")
# button4=Button(bottomFrame,text="button4",fg="purple")
#
# button1.pack(side=LEFT)
# button2.pack(side=LEFT)
# button3.pack(side=LEFT)
# button4.pack(side=BOTTOM)
#
# root.mainloop()


# # Lesson 3
# root = Tk()
#
# one = Label(root, text="One", bg="red", fg="white")
# one.pack()
# two = Label(root, text="Two", bg="green", fg="black")
# two.pack(fill=X)
# three = Label(root, text="Three", bg="blue", fg="white")
# three.pack(side=LEFT, fill=Y)
#
# root.mainloop()


# # Lesson 4-5
# root = Tk()
#
# label_1 = Label(root,text="Name")
# label_2 = Label(root,text="Password")
# entry_1=Entry(root)
# entry_2=Entry(root)
#
# label_1.grid(row=0,sticky=E)
# label_2.grid(row=1,sticky=E)
#
# entry_1.grid(row=0,column=1)
# entry_2.grid(row=1,column=1)
#
# c=Checkbutton(root,text="Keep me logged in")
# c.grid(columnspan=2)
# root.mainloop()


# # Lesson 6
# root = Tk()
#
# # def printName():
# #     print("Hello my name is!")
# #
# # button_1=Button(root, text="Print my name", command=printName)
# # button_1.pack()
#
# def printName(event):
#     print("Hello my name is!")
#
# button_1=Button(root, text="Print my name")
# button_1.bind("<Button-1>",printName)
# button_1.pack()
#
# root.mainloop()


# # Lesson 7
# root = Tk()
#
# def leftClick(even):
#     print("Left")
#
# def middleClick(even):
#     print("Middle")
#
# def rightClick(even):
#     print("Right")
#
# frame = Frame(root,width=300,height=250)
# frame.bind("<Button-1>",leftClick)
# frame.bind("<Button-2>",middleClick)
# frame.bind("<Button-3>",rightClick)
# frame.pack()
#
# root.mainloop()


# # Lesson 8
# class HavenButtons:
#     def __init__(self,master):
#         frame=Frame(master)
#         frame.pack()
#
#         self.printButton=Button(frame,text="Print Message",command=self.printMessage)
#         self.printButton.pack(side=LEFT)
#
#         self.quitButton=Button(frame,text="Quit",command=frame.quit)
#         self.quitButton.pack(side=LEFT)
#
#     def printMessage(self):
#         print("Wow, this actually worked!")
#
# root = Tk()
# b=HavenButtons(root)
# root.mainloop()


# Lesson 12
from Tkinter import *
import tkMessageBox

root = Tk()

tkMessageBox.showinfo("Window Title", "Mountian is high.")

answer=tkMessageBox.askquestion("Question 1", "Do you like fruit?")

if answer == "yes":
    print("  ^_^  ")

root.mainloop()