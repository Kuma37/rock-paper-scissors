from tkinter import *
from PIL import ImageTk, Image
import random as r
root = Tk()
root.title('Rock Paper Scissors')
root.resizable(False, False)

rock = ImageTk.PhotoImage(Image.open('rock1.png'))
scissors = ImageTk.PhotoImage(Image.open('scissors1.png'))
paper = ImageTk.PhotoImage(Image.open('paper1.png'))

l1 = Label(root, text="Welcome to Rock Paper Scissors! Make your choice by pressing the buttons: ")
l1.grid(row=0, column=0, columnspan=3)
score = 0
compscore = 0
flag = 0

def forget():
    l2.destroy()
    l3.destroy()
    l4.destroy()

def rps(choice):
    global compchoice
    compchoice = r.randint(1,3)
    global l2
    global l3
    global l4
    global flag
    global score
    global compscore
    if flag==1:
        forget()
    
    #Printing Choices
    if choice==1:
        l2 = Label(root, text="Your choice: Rock")
        l2.grid(row=1, column=0, columnspan=3)
        flag=1
    elif choice==2:
        l2 = Label(root, text="Your choice: Paper")
        l2.grid(row=1, column=0, columnspan=3)
        flag=1
    else:
        l2 = Label(root, text="Your choice: Scissors")
        l2.grid(row=1, column=0, columnspan=3)
        flag=1
    
    if compchoice==1:
        l3 = Label(root, text="Computer choice: Rock")
        l3.grid(row=2, column=0, columnspan=3)
        flag=1
    elif compchoice==2:
        l3 = Label(root, text="Computer choice: Paper")
        l3.grid(row=2, column=0, columnspan=3)
        flag=1
    else:
        l3 = Label(root, text="Computer choice: Scissors")
        l3.grid(row=2, column=0, columnspan=3)
        flag=1

    #Find result and update score
    if choice==1 and compchoice==2:
        l4 = Label(root, text="Computer Wins! :(")
        l4.grid(row=3, column=0, columnspan=3)
        compscore+=1
    elif choice==2 and compchoice==3:
        l4 = Label(root, text="Computer Wins! :(")
        l4.grid(row=3, column=0, columnspan=3)
        compscore+=1
    elif choice==3 and compchoice==1:
        l4 = Label(root, text="Computer Wins! :(")
        l4.grid(row=3, column=0, columnspan=3)
        compscore+=1
    elif choice==1 and compchoice==3:
        l4 = Label(root, text="You Win! :D")
        l4.grid(row=3, column=0, columnspan=3)
        score+=1
    elif choice==2 and compchoice==1:
        l4 = Label(root, text="You Win! :D")
        l4.grid(row=3, column=0, columnspan=3)
        score+=1
    elif choice==3 and compchoice==2:
        l4 = Label(root, text="You Win! :D")
        l4.grid(row=3, column=0, columnspan=3)
        score+=1
    else:
        l4 = Label(root, text="DRAW :/")
        l4.grid(row=3, column=0, columnspan=3)
    
    scorelabel = Label(root, text="Your score: "+str(score))
    compscorelabel = Label(root, text="Computer score: "+str(compscore))

    scorelabel.grid(row=5, column=0, sticky=W)
    compscorelabel.grid(row=5, column=2, sticky=E)

b1 = Button(root, image=rock, height=75, width=75, command=lambda:rps(1))
b2 = Button(root, image=scissors, height=75, width=75, command=lambda:rps(3))
b3 = Button(root, image=paper, height=75, width=75, command=lambda:rps(2))
exitb = Button(root, text="QUIT", command=root.quit)

b1.grid(row=4, column=0, padx=10, pady=10)
b2.grid(row=4, column=2, padx=10, pady=10)
b3.grid(row=4, column=1, padx=10, pady=10)
exitb.grid(row=5, column=1)

root.mainloop()