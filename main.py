from tkinter import *
from tkinter import messagebox
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"
word={}
timer=None
windows=Tk()
windows.title("Flash Card")
windows.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
messagebox.showinfo(
    title="How to Use",
    message="✅ Click if you know the word — it will be removed from the list.\n"
            "❌ Click if you don't know — the word will appear again later.\n\n"
            "After 3 seconds, the English word will autometiclly be shown.\n"
            "Let's begin!"
)
############## DATA READ ###########
try:
    data=pandas.read_csv(r"D:\python\My codeeess\tkenter\flash_card\data\words_to_learn.csv")
except FileNotFoundError:
    data=pandas.read_csv(r"D:\python\My codeeess\tkenter\flash_card\data\french_words.csv")
word_list=data.to_dict(orient="records")
########### Functions ###########

def current_card():
    global word,timer
    if timer is not None:
        windows.after_cancel(timer)
    word=random.choice(word_list)
    canvas.itemconfig(title, text="French", fill="black")
    canvas.itemconfig(wod,text=word["French"],fill="black")
    canvas.itemconfig(card_bg,image=card_front)
    windows.after(3000,flip_card)

def flip_card():
    canvas.itemconfig(title,text="English",fill="white")
    canvas.itemconfig(wod,text=word["English"],fill="white")
    canvas.itemconfig(card_bg,image=card_back)

def is_known():
    global word_list,word
    word_list=[current_word for current_word in word_list if current_word!=word]
    words_know=pandas.DataFrame(word_list)
    words_know.to_csv(r"D:\python\My codeeess\tkenter\flash_card\data\words_to_learn.csv", index=False)
    current_card()
############ Canvas Setup UI #######################


canvas=Canvas(width=800,height=526, highlightthickness=0,bg=BACKGROUND_COLOR)
card_front=PhotoImage(file=r"D:\python\My codeeess\tkenter\flash_card\card_front.png")
card_back=PhotoImage(file=r"D:\python\My codeeess\tkenter\flash_card\card_back.png")
card_bg=canvas.create_image(400,263,image=card_front)
title=canvas.create_text(400,150,text="French",font=("Ariel",40,"italic"),fill="black")
wod=canvas.create_text(400,263,text="Word",font=("Ariel",60,"bold"),fill="black")
canvas.grid(row=0,column=0,columnspan=2)

################# Images and Button Setup ###################

right_image=PhotoImage(file=r"D:\python\My codeeess\tkenter\flash_card\right.png")
right_button=Button(image=right_image,highlightthickness=0,command=is_known)
right_button.grid(row=1,column=1)

wrong_image=PhotoImage(file=r"D:\python\My codeeess\tkenter\flash_card\wrong.png")
wrong_button=Button(image=wrong_image,highlightthickness=0,command=current_card)
wrong_button.grid(row=1,column=0)
current_card()
windows.mainloop()

