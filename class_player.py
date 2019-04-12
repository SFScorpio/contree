# coding: utf8

from tkinter import *
from class_playmats import *


class player(object):
      
    def __init__(self, window, name, surname = ""):
        self.name = name
        self.surname = surname


class contree_player(player):

    def __init__(self, window, name, surname = ""):
        super().__init__(window, name, surname="")
        self.pgame = []
        
        self.player_frame = ""
        self.xplayed_card = ""
        self.yplayed_card = ""

        self.announcement = ""
        self.pcard = ""
        