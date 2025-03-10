from tkinter import *
import pandas
from random import choice

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE_FONT = ("Ariel", 40, "italic")
WORD_FONT = ("Ariel", 60, "make_bold")

# -------------------------------- READING DATA ----------------------------------------#
try:
    words = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    # converting column -> value, column 2 -> in a dict which in itself is an item in a list
    to_learn = words.to_dict(orient="records")
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas.itemconfig(current_img, image=card_front)
    flip_timer = window.after(3000, flip_card)


def flip_card():
    canvas.itemconfig(current_img, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# -------------------------------- UI ----------------------------------------#
window = Tk()
window.config(pady=50, padx=50, bg=BACKGROUND_COLOR)
window.title("Flashy")
flip_timer = window.after(3000, func=flip_card)

card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
right = PhotoImage(file="images/right.png")
wrong = PhotoImage(file="images/wrong.png")

canvas = Canvas(width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
current_img = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=LANGUAGE_FONT, fill="black")
card_word = canvas.create_text(400, 263, text="", font=WORD_FONT, fill="black")
canvas.grid(row=0, column=0, columnspan=2)
# Buttons
right_button = Button(image=right, highlightbackground=BACKGROUND_COLOR, command=is_known)
right_button.grid(row=1, column=1)
wrong_button = Button(image=wrong, highlightbackground=BACKGROUND_COLOR, command=next_card)
wrong_button.grid(row=1, column=0)

next_card()
window.mainloop()
