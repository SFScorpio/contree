# coding: utf8

from tkinter import *
from PIL import Image, ImageTk


class playmats(object):
    
    def __init__(self):
        self.contree_window = Tk()


class contree_playmats(playmats):
    
    def __init__(self):
        super().__init__()
        self.contree_window.geometry("1200x800")
        self.contree_window.configure(bg="dark green")

        self.tapis_frame = Frame(self.contree_window, bg="green")
        self.tapis_frame.grid()
        self.tapis_frame.place(anchor=NW, x=450, y=250, height=300, width=300)



class player_frame(object):

    def __init__(self, window, name, xlabel, ylabel, xdeck, ydeck):
        self.name_label = Label(window, text=name, bg="red", width=10)
        self.name_label.grid()
        self.name_label.place(anchor=NW, x=xlabel, y=ylabel)

        self.deck_frame = Frame(window, bg="orange")
        self.deck_frame.grid()
        self.deck_frame.place(anchor=NW, x=xdeck, y=ydeck)
       

    def display_cards_button(self, pgame):
        a = 0
        for card in pgame:
            button = Button(self.deck_frame, text=(str(card.name) + card.color), command="")
            but.grid()


    def display_played_card(self, button, window, image, xplayed_card, yplayed_card):
        label_image2 = Label(fra2, image=image)
        label_image2.grid()
        label_image2.place(anchor=NW, x=xplayed_card, y=yplayed_card)

        button.destroy()



