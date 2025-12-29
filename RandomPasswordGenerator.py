length = int(input("Enter the number of characters you'd like in your password:"))

from tkinter import *
import random

window = Tk()
window.title("Random Password Generator")
window.geometry("300x300")
    def generate(letters_cap,letters,numbers,symbols):
    letters_cap = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P"
                   "Q","R","S","T","U","V","W","X","Y","Z"]
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"
                   "q","r","s","t","u","v","w","x","y","z"]
    numbers = [1,2,3,4,5,6,7,8,9,0]
    symbols = ["!","@","#","$","%","^","&","*","(",")","[","]",";",":","'","<",">","?",",","."
               "/","|","+","-","="]
    def randompick(first_random):
        first_random = random.choice[letters_cap,letters,numbers,symbols]
    chosen_letter_cap = random.choice(letters_cap)
    chosen_letter = random.choice(letters)
    chosen_number = random.choice(numbers)
    chosen_symbol = random.choice(symbols)
        
greeting = Label(text="Hello User",fg="black",bg="white")
button = Button(text="Click to Generate Password",fg="white",bg="black")
entry = Entry(fg="yellow",bg="blue",width=50)
greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window,relief=RAISED,borderwidth=5)
frame.pack()
label = Label(master=frame,text="Here's your randomly generated password")
label.pack()

textbox = Text(fg="green",bg="yellow")
textbox.pack()

window.mainloop()