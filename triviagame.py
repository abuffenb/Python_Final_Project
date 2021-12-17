#Python Final Project: December 17, 2021
#Name: Allison Buffenbarger
#I pledge my honor that I have abided by the Stevens Honor System

from tkinter import *
from tkinter import ttk

y = 0

#this creates a notebook that will contain all the frames
a = Tk()
a.title("Disney Trivia")
a.geometry("1500x500")
a = ttk.Notebook()

#this creates the #of frames needed to display
#each question, title page, and final score
frame0 = ttk.Frame(a)
frame1 = ttk.Frame(a)
frame2 = ttk.Frame(a)
frame3 = ttk.Frame(a)
frame4 = ttk.Frame(a)
frame5 = ttk.Frame(a)
frame6 = ttk.Frame(a)
frame7 = ttk.Frame(a)
frame8 = ttk.Frame(a)
frame9 = ttk.Frame(a)
frame10 = ttk.Frame(a)
frame11 = ttk.Frame(a)

#this is the quiz
def trivia(y):

#this adds title tabs to each frame    
    a.add(frame0, text="Welcome")
    a.add(frame1, text="Question 1")
    a.add(frame2, text="Question 2")
    a.add(frame3, text="Question 3")
    a.add(frame4, text="Question 4")
    a.add(frame5, text="Question 5")
    a.add(frame6, text="Question 6")
    a.add(frame7, text="Question 7")
    a.add(frame8, text="Question 8")
    a.add(frame9, text="Question 9")
    a.add(frame10, text="Question 10")
    a.add(frame11, text="Final Score")

#this defines all the questions and the answers to the questions
    Label(frame0, text = "Welcome to the Ultimate Disney Trivia Quiz!", font =("Arial", 50, "bold"), fg = "blue").grid(row=2, column=3)
    
    Label(frame1, text = "What animal was the Sheriff of Nottingham in Disney’s Robin Hood?", font=("Arial", 25, "bold")).grid(row=2, column=1)
    Button(frame1, text = "Rabbit", font=("Arial", 20, "bold"), fg="blue", command=a1_incorrect).grid(row=5, column=1)
    Button(frame1, text = "Gray Wolf", font=("Arial", 20, "bold"), fg="hot pink", command=a1_correct).grid(row=6, column=1)
    Button(frame1, text = "Bengal Tiger", font=("Arial", 20, "bold"), fg="purple", command=a1_incorrect).grid(row=7, column=1)
    Button(frame1, text = "Black Bear", font=("Arial", 20, "bold"), fg="red", command=a1_incorrect).grid(row=8, column=1)
    
    Label(frame2, text = "What are the names of Hades minions in Hercules?", font=("Arial", 25, "bold")).grid(row=2, column=1)
    Button(frame2, text = "Destroy and Destruct", font=("Arial", 20, "bold"), fg="blue", command=a2_incorrect).grid(row=5, column=1)
    Button(frame2, text = "Jim and Bob", font=("Arial", 20, "bold"), fg="hot pink", command=a2_incorrect).grid(row=6, column=1)
    Button(frame2, text = "Pain and Panic", font=("Arial", 20, "bold"), fg="purple", command=a2_correct).grid(row=7, column=1)
    Button(frame2, text = "Violence and Harm", font=("Arial", 20, "bold"), fg="red", command=a2_incorrect).grid(row=8, column=1)

    Label(frame3, text = "Which is the only Disney Princess that has a child?", font=("Arial", 25, "bold")).grid(row=2, column=1)
    Button(frame3, text = "Rapunzel", font=("Arial", 20, "bold"),fg="blue", command=a3_incorrect).grid(row=5, column=1)
    Button(frame3, text = "Ariel", font=("Arial", 20, "bold"), fg="hot pink", command=a3_correct).grid(row=6, column=1)
    Button(frame3, text = "Snow White", font=("Arial", 20, "bold"), fg="purple", command=a3_incorrect).grid(row=7, column=1)
    Button(frame3, text = "Cinderella", font=("Arial", 20, "bold"), fg="red", command=a3_incorrect).grid(row=8, column=1)

    Label(frame4, text = "In the Walt Disney film Pinocchio, what is the name of the giant whale?", font=("Arial", 25, "bold")).grid(row=2, column=1)
    Button(frame4, text = "Monstro", font=("Arial", 20, "bold"), fg="blue", command=a4_correct).grid(row=5, column=1)
    Button(frame4, text = "Norman", font=("Arial", 20, "bold"), fg="hot pink", command=a4_incorrect).grid(row=6, column=1)
    Button(frame4, text = "Marilyn", font=("Arial", 20, "bold"), fg="purple", command=a4_incorrect).grid(row=7, column=1)
    Button(frame4, text = "Blue", font=("Arial", 20, "bold"), fg="red", command=a4_incorrect).grid(row=8, column=1)

    Label(frame5, text = "What is the name of Donald Duck's sister?", font=("Arial", 25, "bold")).grid(row=2, column=1)
    Button(frame5, text = "Daisy Duck", font=("Arial", 20, "bold"), fg="blue", command=a5_incorrect).grid(row=5, column=1)
    Button(frame5, text = "Della Duck", font=("Arial", 20, "bold"), fg="hot pink", command=a5_correct).grid(row=6, column=1)
    Button(frame5, text = "Daphne Duck", font=("Arial", 20, "bold"), fg="purple", command=a5_incorrect).grid(row=7, column=1)
    Button(frame5, text = "Dolores Duck", font=("Arial", 20, "bold"), fg="red", command=a5_incorrect).grid(row=8, column=1)

    Label(frame6, text = "What was Walt Disney’s middle name?", font=("Arial", 25, "bold")).grid(row=2, column=1)
    Button(frame6, text = "Evan", font=("Arial", 20, "bold"), fg="blue", command=a6_incorrect).grid(row=5, column=1)
    Button(frame6, text = "Henry", font=("Arial", 20, "bold"), fg="hot pink", command=a6_incorrect).grid(row=6, column=1)
    Button(frame6, text = "Adam", font=("Arial", 20, "bold"), fg="purple", command=a6_incorrect).grid(row=7, column=1)
    Button(frame6, text = "Elias", font=("Arial", 20, "bold"), fg="red", command=a6_correct).grid(row=8, column=1)

    Label(frame7, text = "In Disney’s 1959 animated film Sleeping Beauty, who is Princess Aurora is betrothed to?", font=("Arial", 25, "bold")).grid(row=2, column=1)
    Button(frame7, text = "Prince Harry", font=("Arial", 20, "bold"), fg="blue", command=a7_incorrect).grid(row=5, column=1)
    Button(frame7, text = "Prince Peter", font=("Arial", 20, "bold"), fg="hot pink", command=a7_incorrect).grid(row=6, column=1)
    Button(frame7, text = "Prince Philip", font=("Arial", 20, "bold"), fg="purple", command=a7_correct).grid(row=7, column=1)
    Button(frame7, text = "Prince Charles", font=("Arial", 20, "bold"), fg="red", command=a7_incorrect).grid(row=8, column=1)

    Label(frame8, text = "What are the names of the three fairies in the Disney classic Sleeping Beauty?", font=("Arial", 25, "bold")).grid(row=2, column=1)
    Button(frame8, text = "Flora, Fauna, and Merryweather", font=("Arial", 20, "bold"), fg="blue", command=a8_correct).grid(row=5, column=1)
    Button(frame8, text = "Flora, Fauna, and Flowers", font=("Arial", 20, "bold"), fg="hot pink", command=a8_incorrect).grid(row=6, column=1)
    Button(frame8, text = "Dahlia, Lilly, and Juniper", font=("Arial", 20, "bold"), fg="purple", command=a8_incorrect).grid(row=7, column=1)
    Button(frame8, text = "Juniper, May, and Flower", font=("Arial", 20, "bold"), fg="red", command=a8_incorrect).grid(row=8, column=1)

    Label(frame9, text = "What was the first ever series to air on the Disney Channel?", font=("Arial", 25, "bold")).grid(row=2, column=1)
    Button(frame9, text = "The Walt Disney Show", font=("Arial", 20, "bold"), fg="blue", command=a9_incorrect).grid(row=5, column=1)
    Button(frame9, text = "Good Morning, Mickey", font=("Arial", 20, "bold"), fg="hot pink", command=a9_correct).grid(row=6, column=1)
    Button(frame9, text = "Storytelling with Walt Disney", font=("Arial", 20, "bold"), fg="purple", command=a9_incorrect).grid(row=7, column=1)
    Button(frame9, text = "Mickey Mouse Clubhouse", font=("Arial", 20, "bold"), fg="red", command=a9_incorrect).grid(row=8, column=1)

    Label(frame10, text = "What is the name of Wendy's dog in Peter Pan?", font=("Arial", 25, "bold")).grid(row=2, column=1)
    Button(frame10, text = "Helen", font=("Arial", 20, "bold"), fg="blue", command=a10_incorrect).grid(row=5, column=1)
    Button(frame10, text = "Spot", font=("Arial", 20, "bold"), fg="hot pink", command=a10_incorrect).grid(row=6, column=1)
    Button(frame10, text = "Puppy", font=("Arial", 20, "bold"), fg="purple", command=a10_incorrect).grid(row=7, column=1)
    Button(frame10, text = "Nana", font=("Arial", 20, "bold"), fg="red", command=a10_correct).grid(row=8, column=1)

    Label(frame11, text="Hope you had fun! You answered correctly:", font=("Arial", 40, "bold"), fg="blue").grid(row=2, column=1)
    Label(frame11, textvariable = total, font=("Arial", 40, "bold"), fg="blue").grid(row=2, column=2)
    Label(frame11, text = "out of 10 times", font=("Arial", 40, "bold"), fg="blue").grid(row=2, column=3)

    #this creates a next button
    #to move to the next frame
    next1_btn = Button(frame0, text = "Next", font =("Arial", 25, "bold"), command = next_1).grid(row=3, column =5)
    frame0.pack
    
    next2_btn = Button(frame1, text = "Next", font =("Arial", 25, "bold"), command = next_2).grid(row=3, column =5)
    frame1.pack
    
    next3_btn = Button(frame2, text = "Next", font =("Arial", 25, "bold"), command = next_3).grid(row=3, column =5)
    frame2.pack
    
    next4_btn = Button(frame3, text = "Next", font =("Arial", 25, "bold"), command = next_4).grid(row=3, column =5)
    frame3.pack
    
    next5_btn = Button(frame4, text = "Next", font =("Arial", 25, "bold"), command = next_5).grid(row=3, column =5)
    frame4.pack
    
    next6_btn = Button(frame5, text = "Next", font =("Arial", 25, "bold"), command = next_6).grid(row=3, column =5)
    frame5.pack
    
    next7_btn = Button(frame6, text = "Next", font =("Arial", 25, "bold"), command = next_7).grid(row=3, column =5)
    frame6.pack
    
    next8_btn = Button(frame7, text = "Next", font =("Arial", 25, "bold"), command = next_8).grid(row=3, column =5)
    frame7.pack
    
    next9_btn = Button(frame8, text = "Next", font =("Arial", 25, "bold"), command = next_9).grid(row=3, column =5)
    frame8.pack
    
    next10_btn = Button(frame9, text = "Next", font =("Arial", 25, "bold"), command = next_10).grid(row=3, column =5)
    frame9.pack
    
    next11_btn = Button(frame10, text = "Next", font =("Arial", 25, "bold"), command = next_11).grid(row=3, column =5)
    frame10.pack

    exit_btn = Button(frame11, text = "Exit", font =("Arial", 40, "bold"), command = exit_actions).grid(row=3, column=4)
    
#this defines the correct and incorrect buttons for each question
#the counter adds up all the correct's individually
def a1_correct():
    Label(frame1, text="Correct :)", font=("Arial", 30, "bold"), bg = "green", fg="white").grid(row=1, column=2)
    counter()
def a1_incorrect():
    Label(frame1, text="Incorrect :(", font=("Arial", 30, "bold"), bg = "red", fg="white").grid(row=1, column=2)

def a2_correct():
    Label(frame2, text="Correct :)", font=("Arial", 30, "bold"), bg = "green", fg="white").grid(row=1, column=2)
    counter()
def a2_incorrect():
    Label(frame2, text="Incorrect :(", font=("Arial", 30, "bold"), bg = "red", fg="white").grid(row=1, column=2)

def a3_correct():
    Label(frame3, text="Correct :)", font=("Arial", 30, "bold"), bg = "green", fg="white").grid(row=1, column=2)
    counter()
def a3_incorrect():
    Label(frame3, text="Incorrect :(", font=("Arial", 30, "bold"), bg = "red", fg="white").grid(row=1, column=2)

def a4_correct():
    Label(frame4, text="Correct :)", font=("Arial", 30, "bold"), bg = "green", fg="white").grid(row=1, column=2)
    counter()
def a4_incorrect():
    Label(frame4, text="Incorrect :(", font=("Arial", 30, "bold"), bg = "red", fg="white").grid(row=1, column=2)

def a5_correct():
    Label(frame5, text="Correct :)", font=("Arial", 30, "bold"), bg = "green", fg="white").grid(row=1, column=2)
    counter()
def a5_incorrect():
    Label(frame5, text="Incorrect :(", font=("Arial", 30, "bold"), bg = "red", fg="white").grid(row=1, column=2)

def a6_correct():
    Label(frame6, text="Correct :)", font=("Arial", 30, "bold"), bg = "green", fg="white").grid(row=1, column=2)
    counter()
def a6_incorrect():
    Label(frame6, text="Incorrect :(", font=("Arial", 30, "bold"), bg = "red", fg="white").grid(row=1, column=2)

def a7_correct():
    Label(frame7, text="Correct :)", font=("Arial", 30, "bold"), bg = "green", fg="white").grid(row=1, column=2)
    counter()
def a7_incorrect():
    Label(frame7, text="Incorrect :(", font=("Arial", 30, "bold"), bg = "red", fg="white").grid(row=1, column=2)

def a8_correct():
    Label(frame8, text="Correct :)", font=("Arial", 30, "bold"), bg = "green", fg="white").grid(row=1, column=2)
    counter()
def a8_incorrect():
    Label(frame8, text="Incorrect :(", font=("Arial", 30, "bold"), bg = "red", fg="white").grid(row=1, column=2)

def a9_correct():
    Label(frame9, text="Correct :)", font=("Arial", 30, "bold"), bg = "green", fg="white").grid(row=1, column=2)
    counter()
def a9_incorrect():
    Label(frame9, text="Incorrect :(", font=("Arial", 30, "bold"), bg = "red", fg="white").grid(row=1, column=2)

def a10_correct():
    Label(frame10, text="Correct :)", font=("Arial", 30, "bold"), bg = "green", fg="white").grid(row=1, column=2)
    counter()
def a10_incorrect():
    Label(frame10, text="Incorrect :(", font=("Arial", 30, "bold"), bg = "red", fg="white").grid(row=1, column=2)

#this is used to count up all the individual correct's
def counter():
    total.set(total.get()+1)

#holds integer value of total counted
#this is returned in frame11 (total score tab)
total = IntVar()

#this define the 'next button' function
def next_1():
    frame1.pack(fill='both')
    frame0.forget()

def next_2():
    frame2.pack(fill='both')
    frame1.forget()

def next_3():
    frame3.pack(fill='both')
    frame2.forget()

def next_4():
    frame4.pack(fill='both')
    frame3.forget()

def next_5():
    frame5.pack(fill='both')
    frame4.forget()

def next_6():
    frame6.pack(fill='both')
    frame5.forget()

def next_7():
    frame7.pack(fill='both')
    frame6.forget()

def next_8():
    frame8.pack(fill='both')
    frame7.forget()

def next_9():
    frame9.pack(fill='both')
    frame8.forget()

def next_10():
    frame10.pack(fill='both')
    frame9.forget()

def next_11():
    frame11.pack(fill='both')
    frame10.forget()

#this exits the program
def exit_actions():
    a.destroy()
    exit()

    
trivia(y)
a.pack()

a.mainloop()
