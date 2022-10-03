BACKGROUND_COLOR = "#B1DDC6"

from tkinter import *
import pandas as pd
import random
import time
new_data = {}
try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    new_data = original_data.to_dict(orient="records")
else:
    new_data = data.to_dict(orient="records")


def new_fashcards():
    global current_card , flip_timer, learned
    window.after_cancel(flip_timer)
    canvas.itemconfig(card_bg, image= front_image)
    current_card = random.choice(new_data)
    canvas.itemconfig(card_title, text="French" , fill ="black")
    canvas.itemconfig(card_word, text= current_card["French"], fill="black")
    flip_timer =window.after(3000, flip_card)

def is_known():
    new_data.remove(current_card)
    df = pd.DataFrame(new_data) 
    df.to_csv('data/words_to_learn.csv', index = False, header=True)
    new_fashcards()
    
    


def flip_card():
    global current_card
    canvas.itemconfig(card_title, text="English", fill = "white" )
    canvas.itemconfig(card_word, text= current_card["English"], fill= "white")
    canvas.itemconfig(card_bg, image= back_image)




window = Tk()
window.title("Flashy")
window.config(padx=50, pady= 50, bg=BACKGROUND_COLOR, highlightthickness=0)
flip_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height= 526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file= "images/card_front.png")
card_bg = canvas.create_image(400, 263,image =  front_image)
back_image = PhotoImage(file= "images/card_back.png")

card_title = canvas.create_text(400, 150, text= "Title", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text= "word", font=("Arial", 60, "bold"))
#canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row= 0, column= 0, columnspan=2)

cross_image = PhotoImage(file = "images/wrong.png")
cross_button = Button(image = cross_image,bg = BACKGROUND_COLOR,  highlightthickness=0, command= new_fashcards)
cross_button.grid(row = 1, column = 0)

right_image = PhotoImage(file = "images/right.png")
right_button = Button(image = right_image,bg = BACKGROUND_COLOR,  highlightthickness=0, command= is_known)
print(right_button)
right_button.grid(row = 1, column = 1)



new_fashcards()


window.mainloop()