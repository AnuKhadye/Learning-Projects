from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

df =pd.read_csv('day-31(Capstone Flash Card)/data/french_words.csv')
df_dict = df.to_dict(orient="records")
current_card = {}



#<------------------------------CHANGE WORDS---------------------------------->
def flip_card():
    canvas.itemconfig(canvas_img,image=card_back_img)
    canvas.itemconfig(title_text,fill="#ffffff")
    canvas.itemconfig(title_text,text="English")
    canvas.itemconfig(card_word,text=current_card["English"])
    canvas.itemconfig(card_word,fill="#ffffff")
    

def next_card():
    global current_card
    if df_dict:
        current_card = random.choice(df_dict)
        print(current_card)
        canvas.itemconfig(canvas_img,image=card_front_img)
        canvas.itemconfig(card_word,text=current_card["French"])
        canvas.itemconfig(title_text,text="French")
        canvas.itemconfig(card_word,fill="#000000")
        canvas.itemconfig(title_text,fill="#000000")
        canvas.after(ms=3000,func=flip_card)
        
def known_card_discard():
    df_dict.remove(current_card)
    pd.DataFrame(df_dict).to_csv('day-31(Capstone Flash Card)/data/french_words_known_removed.csv', index=False)
    next_card()

#<------------------------------UI SETUP---------------------------------->

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50,bg=BACKGROUND_COLOR)

canvas = Canvas(width=800, height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card_front_img = PhotoImage(file="day-31(Capstone Flash Card)/images/card_front.png")
card_back_img = PhotoImage(file="day-31(Capstone Flash Card)/images/card_back.png")
canvas_img = canvas.create_image(400, 263, image=card_front_img)

title_text = canvas.create_text(400,150,text="Title", font=("Ariel",42,"italic"))
card_word = canvas.create_text(400,263,text="word",font=("Ariel",60,"bold"))
canvas.grid(column=0,row=0,columnspan=2)

cross_image = PhotoImage(file="day-31(Capstone Flash Card)/images/wrong.png")
cross_button = Button(image=cross_image,highlightthickness=0,command=next_card)
cross_button.grid(column=1,row=1)

tick_image = PhotoImage(file="day-31(Capstone Flash Card)/images/right.png")
tick_button = Button(image=tick_image,highlightthickness=0,command=known_card_discard)
tick_button.grid(column=0,row=1)

next_card()

window.mainloop()