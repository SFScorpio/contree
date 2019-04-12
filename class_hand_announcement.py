# coding: utf8

from class_game import *
from class_hand_score import *
from contree_data import *
from class_hand_going import *
from tkinter.ttk import Combobox


class hand_announcement(object):
    
    def __init__(self, dealer, player, pack, team):
        self.value = ("80", "90", "100", "110", "120", "130", "140", "150", "160", "capot", "passe", "contree", "sur-contree")

        self.announcement = []
        self.dealer = dealer
        self.starter = ""
        self.players_list = player
        self.hand_team = team
        self.team_taker = ""
        self.pack = pack
        self.hand_master = ""
        self.team_master = ""
        self.combobox_list = []
        self.button_dico = {}


    def player_team(self, index_announcer):
        for pt in self.hand_team:
            if self.players_list[index_announcer] in pt.team:
                return pt


    def def_dealer(self, hand_number):
        self.dealer = self.players_list[(self.players_list.index(self.dealer) + hand_number) % 4]
        self.dealing(self.dealer, self.def_starter())


    def def_starter(self):
        self.starter = self.players_list[(self.players_list.index(self.dealer) + 1) % 4]
        return self.starter
    
    
    def dealing(self, dealer, starter):
        pack = self.pack
        index_announcer = self.players_list.index(starter)
        while len(pack) != 0:
            self.players_list[index_announcer % 4].pgame.append(pack.pop())
            index_announcer += 1


    def display_card_button(self, frame):
        for player in self.players_list:
            a=0
            for card in player.pgame:
                print(a)
                self.button_dico[card] = Button(player.player_frame.deck_frame, image=card.face, command=lambda: player.player_frame.display_played_card(self.button_dico[card], frame, card.face, player.xplayed_card, player.yplayed_card))
                self.button_dico[card].grid(row=a)
                a+=1


    def create_announcement_combobox(self, item, frame, xcombobox, ycombobox, var):
        announcement_combobox = Combobox(frame, width=10, textvariable=var)
        announcement_combobox['values'] = item
        announcement_combobox.grid()
        announcement_combobox.place(anchor=NW, x=xcombobox, y=ycombobox)
        self.combobox_list += [announcement_combobox]


    def destroy_button(self, button_list):
        for button in button_list:
            button.destroy()
        button_list = []


    def display_announcement_and_speaker(self, frame, index_announcer):
        if len(self.announcement) > 1:
            for player in self.players_list:
                if player.announcement == self.announcement:
                    self.announcement_label.config(text="{0} announced {1}".format(player.name, self.announcement))
            
        else:
            self.announcement_label = Label(frame, text="You're first to announce")
            self.announcement_label.grid()
            self.announcement_label.place(anchor=NW, x=50, y=20)

        speaker_label = Label(frame, text=self.players_list[index_announcer].name + " your turn to annouce")
        speaker_label.grid()
        speaker_label.place(anchor=NW, x=50, y=60)


    def input_announcement(self, color, value, index_announcer, frame):
        self.display_announcement_and_speaker(frame, index_announcer)

        announcement_value = StringVar()
        self.create_announcement_combobox(value, frame, 25, 100, announcement_value)

        announcement_color = StringVar()
        self.create_announcement_combobox(color, frame, 160, 100, announcement_color)

        announ_button = Button(frame, text="GO", height=1, width=10, command=lambda: self.return_announcement(color, value, index_announcer, frame, announcement_value.get(), announcement_color.get()))
        announ_button.grid()
        announ_button.place(anchor=NW, x=110, y=200)


    def return_announcement(self, color, value, index_announcer, frame, announcement_value, announcement_color):

        self.destroy_button(self.combobox_list)
        
        print(announcement_value, type(announcement_value), "===", announcement_color)

        if announcement_value in  self.value[-3:]:
            print("++++1", self.players_list[index_announcer].announcement)
            self.players_list[index_announcer].announcement = announcement_value
            print(12, self.players_list[index_announcer].announcement)
            self.check_announcement(color, value, index_announcer, self.players_list[index_announcer].announcement, frame)

        else:
            self.players_list[index_announcer].announcement = [announcement_value, announcement_color]
            print("++++2", self.players_list[index_announcer].announcement)
            self.check_announcement(color, value, index_announcer, self.players_list[index_announcer].announcement, frame)


    def check_announcement(self, color, value, index_announcer, announcement, frame):
        print(13, announcement)
        if announcement == "passe":
            print("====", 1, "====")
            self.announcement
            self.check_continue_announce(color, value, index_announcer, frame)

        elif announcement == "sur-contree":
            print("====", 2, "====")
            self.announcement[2] = "sur-contree"
            self.players_list[index_announcer].announcement = self.announcement
            self.check_continue_announce(color, value, index_announcer, frame)
        
        elif announcement == "contree":
            print("====", 3, "====")
            self.announcement = self.announcement + ["contree"]
            self.players_list[index_announcer].announcement = self.announcement
            self.check_continue_announce(color, value, index_announcer, frame)

        elif type(announcement) is list and len(announcement) >= 2 and announcement[0] in value and announcement[1] in color:
            print("====", 4, "====")
            self.announcement = announcement
            self.check_continue_announce(color, value, index_announcer, frame)

        else:
            print("====", 5, "====")
            return self.input_announcement(color, value, index_announcer, frame)


    def check_continue_announce(self, color, value, index_announcer, frame):
        if "sur-contree" in self.players_list[index_announcer].announcement:
            self.start_playing_hand()
            
        elif self.players_list[index_announcer].announcement == "passe":
            self.end_announcement(index_announcer, frame)
            
        elif self.players_list[index_announcer].announcement != "passe":
            self.player_team(index_announcer).announcement = self.players_list[index_announcer].announcement
            index_announcer = (index_announcer + 1) % 4
            self.announce(color, index_announcer, frame)


    def end_announcement(self, index_announcer, frame):
        if self.players_list[index_announcer].announcement == "passe" and self.players_list[(index_announcer + 3) % 4].announcement == "passe" and self.players_list[(index_announcer + 2) % 4].announcement == "passe" and self.players_list[(index_announcer + 1) % 4].announcement == "passe":
            playhand = hand_going(self.atout) # ===== to mofify

        elif self.announcement != [] and self.players_list[index_announcer].announcement == "passe" and self.players_list[(index_announcer + 3) % 4].announcement == "passe" and self.players_list[(index_announcer + 2) % 4].announcement == "passe":
            self.start_playing_hand()

        else:
            index_announcer = (index_announcer + 1) % 4
            self.announce(color, index_announcer, frame)
        
    
    def list_announcement(self, index_announcer):
        if type(self.announcement) == list and len(self.announcement) == 2 and self.announcement[0] in self.value:
            print("====", 2)
            return self.value[self.value.index(self.announcement[0]) + 1:]
        elif type(self.announcement) == list and len(self.announcement) == 3 and self.announcement[2] == "contree":
            print("====", 3)
            return [self.value[-1], self.value[-3]]
        else:
            print("====", 4)
            return self.value[:-2]


    def announce(self, color, index_announcer, frame):
        value = self.list_announcement(index_announcer)
        print("last announcement", self.announcement)
        print("index_announcer: ", index_announcer)
        print(value)
        print(self.players_list[index_announcer].name)

        self.players_list[index_announcer].announcement = self.input_announcement(color, value, index_announcer, frame)


    def start_playing_hand(self):
        print("before", self.announcement)
        self.def_team_taker()
        playhand = hand_going(self.atout, self.players_list, self.hand_team, self.team_taker, self.starter)
        playhand.play_hand(atout_order, normal_order)




    def def_team_taker(self):
        for tt in self.hand_team:
            if self.announcement == tt.announcement:
                self.team_taker = tt
        self.def_atout()
        for player in self.players_list:
            player.announcement = ""


    def other_team(self): 
        for team in self.hand_team:
            if team != self.team_taker:
                return team


    def def_atout(self):
        self.atout = self.announcement[1]


