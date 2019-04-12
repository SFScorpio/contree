# coding: utf8

from cards import *
from tkinter import *
from contree_data import *
from class_button import *

class cards(object):
    
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
        self.face = ""
        self.tail = "/Users/nic/Desktop/python/contree/cards/tail.png"


    def card_figure(self):
        if self.color == "spade":
            fcolor = "pique"
        elif self.color == "heart":
            fcolor = "coeur"
        elif self.color == "diamond":
            fcolor = "carreau"
        elif self.color == "club":
            fcolor = "treffle"
        
        if self.name == "JACK":
            value = "valet"
        elif self.name == "QUEEN":
            value = "reine"
        elif self.name == "KING":
            value = "roi"
        elif self.name == "AS":
            value = "as"
        else:
            value = self.name
        image = PhotoImage(file="/Users/nic/Desktop/python/contree/cards/" + (str(value) + '_' + fcolor + ".png"))
        self.face = image.subsample(11, 11)



class contree_card(cards):
    
    
    def __init__(self, name, color):
        super().__init__(name, color)
        self.card_score_value = 0
    
   
    def normal_score_card(self):
        if self.name == "10":
            return different_score_value[4]
        elif self.name == "JACK":
            return different_score_value[1]
        elif self.name == "QUEEN":
            return different_score_value[2]
        elif self.name == "KING":
            return different_score_value[3]
        elif self.name == "AS":
            return different_score_value[5]
        else:
            return different_score_value[0]


    def atout_score_card(self):
        if self.name == "9":
            return different_score_value[6]
        elif self.name == "JACK":
            return different_score_value[7]