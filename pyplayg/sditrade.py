#!/usr/bin/python

from Tkinter import *

root = Tk()
frame = Frame(root)
frame.pack()

bottomframe = Frame(root)
bottomframe.pack( side = BOTTOM )

redbutton = Button(frame, text="Red", fg="red")
redbutton.pack( side = LEFT)

greenbutton = Button(frame, text="Brown", fg="brown")
greenbutton.pack( side = LEFT )

bluebutton = Button(frame, text="Blue", fg="blue")
bluebutton.pack( side = LEFT )

blackbutton = Button(bottomframe, text="Black", fg="black")
blackbutton.pack( side = BOTTOM)

def onclick():
   pass

text = Text(root)
text.insert(INSERT, "Hello.....")
text.insert(END, "Bye Bye.....")
text.pack()

text.tag_add("here", "1.0", "1.4")
text.tag_add("start", "1.8", "1.13")
text.tag_config("here", background="yellow", foreground="blue")
text.tag_config("start", background="black", foreground="green")

def donothing():
   filewin = Toplevel(root)
   button = Button(filewin, text="Do nothing button")
   button.pack()
   
def save1():
	print("First Name: %s\nLast Name: %s" % (e1g.get(), e2g.get()))   
def test1():
	print("First Name: %s\nLast Name: %s" % (e1g.get(), e2g.get()))  	
e1g= StringVar()
e2g= StringVar()
   
def donothing2():
   filewin = Toplevel(root)
   Label(filewin, text="First Name").grid(row=0)
   Label(filewin, text="Last Name").grid(row=1)
   e1 = Entry(filewin,textvariable=e1g)
   e2 = Entry(filewin,textvariable=e2g)
   e1.grid(row=0, column=1)
   e2.grid(row=1, column=1)
   button = Button(filewin, text="Save",command=save1).grid(row=2, column=0, sticky=W, pady=4)
   button2 = Button(filewin, text="Test" ,command=test1).grid(row=2, column=1, sticky=W, pady=4)
   

   
   
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=donothing2)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

Lb1 = Listbox(root,selectmode=SINGLE)
Lb1.insert(1, "LTC_USD")
Lb1.insert(2, "BTC_LTC")
Lb1.insert(3, "BTC_USD")

Lb1.pack()

var = StringVar()
label = Label( root, textvariable=var, relief=RAISED )

var.set("Hey!? How are you doing?")
label.pack()

C = Canvas(root, bg="blue", height=250, width=300)

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start=0, extent=150, fill="red")

C.pack()
root.mainloop()


