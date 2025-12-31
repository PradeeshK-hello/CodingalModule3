from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Denomination Calculator")
root.config(bg="light blue")
root.geometry("650x400")

upload = Image.open("Cash.png")
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)
label = Label(root,image=image,bg="light blue")
label.place(x=180,y=20)

label1 = Label(root,
               text="Hey User! Welcome to the Denomination Counter Application.",
               bg="light blue")
label1.place(relx=0.5,y=340,anchor=CENTER)

def msg():
    MsgBox = messagebox.showinfo(
    "Alert","Do you want to calculator the denomination count?")
    if MsgBox == "ok":
        topwin()

button1 = Button(root,
                 text="Let's get started!",
                 command=msg,
                 bg="brown",
                 fg="white")
button1.place(x=260,y=360)

def topwin():
    top = Toplevel()
    top.title("Denominations Calculator")
    top.config(bg="light grey")
    top.geometry("600x350+50+50")
    
    label = Label(top,text="Enter total amount",bg="light grey")
    entry = Entry(top)
    lbl = Label(top, text="Here are the numbers of notes for each denomination", bg="light grey")
    
    l1 = Label(top, text="100",bg="light grey")
    l2 = Label(top, text="50",bg="light grey")
    l3 = Label(top, text="10",bg="light grey")
    l4 = Label(top, text="5",bg="light grey")
    l5 = Label(top, text="2",bg="light grey")
    l6 = Label(top, text="1",bg="light grey")
    l7 = Label(top, text="0.50",bg="light grey")
    l8 = Label(top, text="0.20",bg="light grey")
    l9 = Label(top, text="0.10",bg="light grey")
    l10 = Label(top, text="0.05",bg="light grey")
    
    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    t4 = Entry(top)
    t5 = Entry(top)
    t6 = Entry(top)
    t7 = Entry(top)
    t8 = Entry(top)
    t9 = Entry(top)
    t10 = Entry(top)

    def calculator():
        try:
            global amount
            amount = float(entry.get())
            note100 = amount//100
            amount = 100
            note50 = amount//50
            amount = 50
            note10 = amount//10
            amount = 10
            
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            
            t1.insert(END, str(note100))
            t2.insert(END, str(note50))
            t3.insert(END, str(note10))
            
        except ValueError:
            messagebox.showerror("Error","Please enter a valid value.")
            
    btn = Button(top,text="Calculate",command=calculator,bg="brown",fg="white")
    
    label.place(x=230,y=50)
    entry.place(x=200,y=80)
    btn.place(x=240,y=120)
    lbl.place(x=140,y=170)
    
    l1.place(x=180,y=200)
    l2.place(x=180,y=230)
    l3.place(x=180,y=260)
    
    t1.place(x=270,y=200)
    t2.place(x=270,y=230)
    t3.place(x=270,y=260)
    
    top.mainloop()
root.mainloop()