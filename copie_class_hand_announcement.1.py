# coding: utf8

from class_game import *
from class_hand_score import *
from contree_data import *


class hand_announcement(object):
    
    def __init__(self, dealer, player, pack, team):
        self.starter = ""
        self.announcement = []
        self.dealer = dealer
        self.starter = ""
        self.player = player
        self.hteam = team
        self.team_taker = ""
        self.pack = pack
        self.hand_master = ""
        self.team_master = ""
        self.value_button_list = []
        self.color_button_list = []


    def player_team(self, a):
        for pt in self.hteam:
            if self.player[a] in pt.team:
                return pt


    def def_dealer(self, hand_number):
        self.dealer = self.player[(self.player.index(self.dealer) + hand_number) % 4]
        self.dealing(self.dealer, self.def_starter())


    def def_starter(self):
        self.starter = self.player[(self.player.index(self.dealer) + 1) % 4]
        return self.starter
    
    
    def dealing(self, dealer, starter):
        pack = self.pack
        a = self.player.index(starter)
        while len(pack) != 0:
            self.player[a % 4].pgame.append(pack.pop())
            a += 1


    def create_announcement_value_buton(self, avalue, frame):
        column = 0
        for value in avalue:
            value = announcement_value_button(frame, value, column)
            self.value_button_list += [value.button]
            column += 1


    def create_announcement_color_buton(self, color, frame):
        column = 0
        for item in color:
            item = announcement_color_button(frame, item, column)
            self.color_button_list += [item.button]
            column += 1


    def input_announcement(self, col, val, a, frame):
            self.create_announcement_value_buton(val, frame)
            self.create_announcement_color_buton(col, frame)

            announ = Button(frame, text="GO", height=1, width=10, command = "")
            announ.grid(column=2, row=3)
            a = input()

    def return_announcement(self):
        return print("xxxxx")
    
    
    def code_announcement(self, announ): # ==== to verify utility
        if ',' in announ:
            announ = announ.split(',')
            if announ[0].isdigit():
                announ = [int(announ[0]), announ[1].strip()]
        else:
            announ = announ.strip()
        return announ
            
    def check_announcement(self, col, val, a, announ, frame):
        if  announ == "passe":
            return announ
        elif announ == "sur-contree":
            self.announcement[2] = "sur-contree"
            announ = self.announcement
            return announ
        elif  announ == "contree":
            announ = self.announcement + ["contree"]
            return announ
        elif type(announ) is list and len(announ) >= 2 and announ[0] in val and announ[1] in col:
            return announ
        else:
            return self.input_announcement( col, val, a, frame)
        
    
    def list_announcement(self, t, tval, announ, value):
        if announ == "passe":
            return [value[-1], value[-3]]
        elif type(announ) == list and len(announ) == 2 and announ[0] in tval:
            return value[value.index(announ[0]) + 1:]
        elif type(announ) == list and len(announ) == 3 and announ[2] == "contree":
            return [value[-1], value[-3]]
        else:
            return value[:-2]


    def announce(self, Value, Color, starter, h, frame):
        the_show_must_go_on = True
        a = self.player.index(starter)
        val = Value
        print("hand number", h)
        
        while the_show_must_go_on:
            pteam = self.player_team(a)
            val = self.list_announcement(pteam, val, self.announcement, Value)
            self.player[a].announcement = self.input_announcement(Color, val, a, frame)
            print("player", self.player[a].announcement)
            print("announcement", self.announcement)
            if "sur-contree" in self.player[a].announcement:
                the_show_must_go_on = False
                
            elif self.player[a].announcement == "passe":
                the_show_must_go_on = self.end_announcement(a)
                
            elif self.player[a].announcement != "passe":
                self.announcement = self.player[a].announcement
                pteam.announcement = self.player[a].announcement
                         
            a = (a + 1) % 4
        self.def_team_taker()
        for player in self.player:
            player.announcement = ""



    def def_team_taker(self):
        if self.announcement != []:
            for tt in self.hteam:
                if self.announcement == tt.announcement:
                    self.team_taker = tt
            self.def_atout()


    def other_team(self): 
        for team in self.hteam:
            if team != self.team_taker:
                return team


    def def_atout(self):
        self.atout = self.announcement[1]


    def end_announcement(self, a):
        if self.player[a].announcement == "passe" and self.player[(a + 3) % 4].announcement == "passe" and self.player[(a + 2) % 4].announcement == "passe" and self.player[(a + 1) % 4].announcement == "passe":
            return False
        elif self.announcement != [] and self.player[a].announcement == "passe" and self.player[(a + 3) % 4].announcement == "passe" and self.player[(a + 2) % 4].announcement == "passe":
            return False
        else:
            return True