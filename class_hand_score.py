# coding: utf8

from cards import *
from contree_data import *

print("coucou")
class hand_score(object):
    
    def __init__(self, other_team, team_taker):
        self.other_team = other_team
        self.team_taker = team_taker
        self.team_taker_hand_score_without_belote = 0


    def calcul_team__score(self, specific_announcement_score_value, announ, atout):
        if announ[0] == "capot":
            score = pecific_announcement_score_value[2] * self.multiple_factor()
            
            if self.announce_done(announ, atout):
                self.team_taker.score += score
            else:
                self.other_team.score += score
    
        elif "contree" in announ or "sur-contree" in announ:
            score = specific_announcement_score_value[0] * self.multiple_factor()
            
            if self.announce_done(announ, atout):
                self.team_taker.score += score
            else:
                self.other_team.score += score
        
        elif self.announce_done(announ, atout) == False:
            self.other_team.score += specific_announcement_score_value[0]
            
        else:
            self.team_taker.score += team_taker_hand_score_without_belote + self.belote_score(self.team_taker)
            self.other_team.score += (specific_announcement_score_value - team_taker_hand_score_without_belote) + self.belote_score(self.other_team)
        print("announce: {0}\
              \n team taker score: , {1},\
              \n{2}, {3}\
              \n {4}: {5}".format(announ,\
                  self.announce_done(announ, atout),\
                  self.team_taker,\
                  self.team_taker.score,\
                  self.other_team,\
                  self.other_team.score))
    
    
    def multiple_factor(self):
        if "contree" in self.announcement:
            return 2
        elif "sur-contree" in self.announcement:
            return 4
        else:
            return 1
    
    
    def announce_done(self, announ, atout):
        if announ[0] == "capot":
            if len(self.team_taker.round_win) == 32:
                return True
        else:
            self.calcul_team_taker_hand_score(atout)
            if self.team_taker_hand_score_without_belote + self.belote_score(self.team_taker) >= announ[0]:
                return True
            else:
                return False
    
    
    def calcul_team_taker_hand_score(self, atout):
        score = 0
        for card in self.team_taker.round_win:
            score += self.score_card(card, atout) + self.last_turn_score(self.team_taker)
        self.team_taker.round_win, self.other_team.round_win = [], []
    
    
    def score_card(self, card, atout):
        if card.color == atout and (card.name == "9" or card.name == "JACK"):
            return card.atout_score_card()
        else:
            return card.card_score_value
    
    
    def belote_score(self, team):
        if team.belote == "yes":
            return different_score_value[7]
        else:
            return 0
    
    
    def last_turn_score(self, team):
        if team.last_turn == "yes":
            return different_score_value[4]
        else:
            return 0



