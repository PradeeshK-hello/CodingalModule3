from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("Rock Paper Scissors")
root.geometry("300x250")

def play(user_choice):
    choices = ["Rock","Paper","Scissors"]
    comp_choice = random.choice(choices)
    if user_choice == comp_choice:
        result = "It's a Tie!"
    elif (user_choice == "Rock" and comp_choice == "Scissors"):
        result = "You Win!"
    elif (user_choice == "Paper" and comp_choice == "Rock"):
        result = "You Win!"
    elif (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "You Win!"
    else:
        result = "Computer Wins!"
    messagebox.showinfo("Result",
     f"You chose: {user_choice}\nComputer chose: {comp_choice}\n\n{result}")

Label(root, text="Rock Paper Scissors",
      font=("Palatino Linotype",16,"bold")).pack(pady=10)

Button(root, text="Rock",width=15,command=lambda:play("Rock")).pack(pady=5)
Button(root, text="Paper",width=15,command=lambda:play("Paper")).pack(pady=5)
Button(root, text="Scissors",width=15,command=lambda:play("Scissors")).pack(pady=5)

root.mainloop()