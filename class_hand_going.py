# coding: utf8

class hand_going(object):

    def __init__(self, atout, players, team, taker, starter):
        self.atout = atout
        self.players_list = players
        self.hand_team = team
        self.hand_played_card = []
        self.team_taker = taker
        self.starter = starter


    def play_hand(self, aorder, norder):
        for played_turn in range(8):
            a = self.round_starter(played_turn)
            hand_played_card = 0
            print("======== next hand ========")
            while hand_played_card < 4:
                print("\n \n \n atout color: ", self.atout)
                print("card played: ", [(card.name, card.color) for card in self.hand_played_card])
                print("player", a, self.players_list[a].name)
                card = self.players_list[a].pgame.pop(self.players_list[a].pgame.index(self.choosen_card(a, aorder)))
                self.def_hand_master(a, card, aorder, norder)
                self.def_team_master()
                self.players_list[a].pcard = card
                self.hand_played_card += [card]
                a = (a + 1) % 4
                hand_played_card += 1
                print(card.name, card.color)
                
            self.def_last_turn_team(played_turn)
            played_turn += 1
            self.keep_round_card()


    def belote(self):
        for player in self.players_list:
            cbelote = 0
            for card in player.pgame:
                if card.name == "QUEEN" and card.color == self.atout:
                    cbelote += 1
                elif card.name == "KING" and card.color == self.atout:
                    cbelote += 1
            if cbelote == 2:
                for team in self.hand_team:
                    if player in team:
                        self.hand_team.belote = "yes"
            

    def round_starter(self, played_turn):
        if played_turn == 0:
            return self.players_list.index(self.starter)
        else:
            self.starter = self.hand_master
            return self.players_list.index(self.hand_master)
    
    def choosen_card(self, a, aorder):
        print("{0}\
              \nyour game is: {1} \nwich card do you wanna play:\
              \n(just enter the number separated by a comma)".format(self.players_list[a].name, list((card.name, card.color) for card in sorted(self.players_list[a].pgame, key = lambda a: a.color))))
        crd = input().split(',')       
        fcard = self.convert_card(crd, a)
 
        return self.authorised_card(a, fcard, aorder)

    
    def convert_card(self, crd, a):
        for tcrd in self.players_list[a].pgame:
            if crd[0].isdigit():
                if tcrd.name == int(crd[0]) and tcrd.color == crd[1].strip():
                    return tcrd
            elif tcrd.name == crd[0].upper() and tcrd.color == crd[1].strip():
                    return tcrd


    def authorised_card(self, a, card, aorder):
        if self.hand_played_card == []:
            return card
        
        else:
            if card.color == self.starter.pcard.color:
                if self.starter.pcard.color == self.atout and self.higher_atout_value(card, self.hand_master.pcard, aorder) == False:
                    return self.atout_greater_than_master(card, a, aorder)
                else:
                    return card
            
            elif card.color != self.starter.pcard.color and self.no_color(a) == False:
                return self.choosen_card(a, aorder)
            
            elif card.color != self.atout:
                if self.players_list[a] not in self.team_master.team and self.no_atout(a) == False:
                    return self.atout_greater_than_master(card, a, aorder)
                else:
                    return card
    
            elif card.color == self.atout:
                if  self.hand_master.pcard.color == self.atout and self.higher_atout_value(card, self.hand_master.pcard, aorder) == False:
                    return self.atout_greater_than_master(card, a, aorder)
                else:
                    return card
    
            else:
                return card


    def atout_greater_than_master(self,card, a, aorder):
        if self.hand_master.pcard.color == self.atout and self.higher_atout(a, aorder) == False:
            return self.choosen_card(a, aorder)
        else:
            return card


    def higher_atout(self, a, aorder):
        for card in self.players_list[a].pgame:
            if card.color == self.atout and self.higher_atout_value(card, self.hand_master.pcard, aorder):
                print("&&&&&&")
                return False
    
    
    def def_team_master(self):
        for t in self.hand_team:
            if self.hand_master in t.team:
                self.team_master = t


    def def_last_turn_team(self, played_turn):
        if played_turn == 7:
            self.team_master.last_turn = "yes"


    def no_color(self, a):
        for card in self.players_list[a].pgame:
            if card.color == self.starter.pcard.color:
                return False
    
    
    def no_atout(self, a):
            for card in self.players_list[a].pgame:
                if self.atout == card.color:
                    return False 


    def def_hand_master(self, a, card, aorder, norder):
        if self.hand_played_card == []:
            self.hand_master = self.players_list[a]
            
        elif card.color == self.atout:
            if self.hand_master.pcard.color == self.atout:
                if self.higher_atout_value(card, self.hand_master.pcard, aorder) == True:
                    self.hand_master = self.players_list[a]
            else:
                self.hand_master = self.players_list[a]
                
        elif self.higher_normal_value(card, self.hand_master.pcard, norder):
            self.hand_master = self.players_list[a]


    def higher_atout_value(self, fstcard, seccard, aorder):
        print(fstcard.name, "===", seccard.name)
        if aorder.index(fstcard.name) > aorder.index(seccard.name):
            return True
        else:
            return False

    
    def higher_normal_value(self, fstcard, seccard, norder):
        print(fstcard.name, "===", seccard.name)
        if fstcard.color == seccard.color:
            if norder.index(fstcard.name) < norder.index(seccard.name):
                return False


    def keep_round_card(self):
        self.team_master.round_win += self.hand_played_card
        self.hand_played_card = []
        for player in self.players_list:
            player.pcard = ""


    def refill_pack(self, pack):
       for team in self.hand_team:
           pack += team.round_win
           team.round_win == []