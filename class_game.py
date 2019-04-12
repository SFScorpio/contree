# coding: utf8

from random import shuffle, choice, randrange
from tkinter import *
import PIL.Image, PIL.ImageTk
from class_card import *
from class_player import *
from class_team import *
from class_button import *



class game(object):
    
    def __init__(self, sl = 2000):
        self.pack = []
        self.player = []
        self.team = []
        self.score_limit = sl
        self.dealer = ""
        self.hand_number = 0
        

    def pack_game(self, tapis, cname, color):
        a = 0
        for col in color:
            for val in cname[5:]:
                name = contree_card(val, col)
                name.card_figure()
                name.card_score = name.normal_score_card()
                self.pack += [name]
                a += 1
        return self.pack
        

    def def_team(self):
        team1, team2 = teams(), teams()
        team1.team, team2.team = [self.player[0], self.player[2]], [self.player[1], self.player[3]] 
        self.team += (team1, team2)


    def shuffle_card(self):
        shuffle(self.pack)
        return self.split_pack()


    def split_pack(self):
        a = randrange(2,len(self.pack)-1)
        self.pack = self.pack[a:] + self.pack[:a]
        return self.pack


    def first_dealer(self):
        l = []
        self.shuffle_card()
        for player in self.player:
            player.pgame.append(self.pack.pop(self.pack.index(choice(self.pack))))
            l.append(player.pgame[0])
        bcard = self.sorted_card(l, cname)
        for player in self.player:    
            if player.pgame[0] == bcard:
                self.dealer =  player
        self.add_card()


    def sorted_card(self, l, cname):
        bcard = ""
        for card in l:
            print("==", card.name, card.color)
            if bcard == "":
                bcard = card
            elif cname.index(card.name) > cname.index(bcard.name):
                bcard = card
            elif cname.index(card.name) == cname.index(bcard.name):
                bcard = self.check_color(card, bcard)
        return bcard


    def check_color(self, card, bcard):
        l = [card, bcard]
        for ccard in l:
            if ccard.color == "spade":
                return ccard
            elif ccard.color == "heart":
                return ccard
            elif ccard.color == "diamon":
                return ccard


    def add_card(self):
        for player in self.player:
            self.pack += player.pgame
            player.pgame = []


    def create_player(self, window, name_1, name_2, name_3, name_4):
        player_1 = contree_player(window=window, name=name_1)
        player_1.player_frame = player_frame(window=window, name=player_1.name, xlabel=550, ylabel=50, xdeck=500, ydeck=100)
        player_1.xplayed_card, player_1.yplayed_card= 115, 0

        player_2 = contree_player(window=window, name=name_2)
        print(type(player_1))
        player_2.player_frame = player_frame(window=window, name=player_2.name, xlabel=45, ylabel=400, xdeck=100, ydeck=200)
        player_2.xplayed_card, player_2.yplayed_card= 30, 100

        player_3 = contree_player(window=window, name=name_3)
        player_3.player_frame = player_frame(window=window, name=player_3.name, xlabel=550, ylabel=600, xdeck=400, ydeck=650)
        player_2.xplayed_card, player_2.yplayed_card= 115, 200

        player_4 = contree_player(window=window, name=name_4)
        player_4.player_frame = player_frame(window=window, name=player_4.name, xlabel=1050, ylabel=400, xdeck=1050, ydeck=200)
        player_2.xplayed_card, player_2.yplayed_card= 200, 100

        self.player = [player_1, player_2, player_3, player_4]


    def start_game(self, cname, color, window, name_1, name_2, name_3, name_4):
        self.create_player(window, name_1, name_2, name_3, name_4)
        self.pack_game(window, cname, color)
        self.first_dealer()
        self.def_team()
    

