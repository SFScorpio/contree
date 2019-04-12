import os.path
from tkinter import *
from PIL import *
from choose_game import *
from class_game import *
from class_player import *
from contree_data import *
from class_hand_announcement import *
from class_hand_going import *
from class_card import *
from class_playmats import *
from cards import *

tapis = contree_playmats()
tw = tapis.contree_window

entry_player = "======="

name_1 = "nico"
name_2 = "franck"
name_3 = "ste"
name_4 = "man"

g = game()
g.start_game(cname, color, tw, name_1, name_2, name_3, name_4)

#while g.team[0].score < g.score_limit or g.team[1].score < g.score_limit:
g.hand_number += 1
print("dealer", g.dealer.name)

print("hand: ", g.hand_number)

hand_announce = hand_announcement(g.dealer, g.player, g.pack, g.team)
hand_announce.def_dealer(g.hand_number)

hand_announce.display_card_button(tw)
hand_announce.announce(color, g.player.index(hand_announce.starter), tapis.tapis_frame)
    
if hand_announce.announcement != []:
    
    
    score = hand_score(hand_announce.team_taker, hand_announce.other_team())
    score.calcul_team__score(specific_announcement_score_value, hand_announced.announcement, hand_announce.atout)
    playhand.refill_pack(hand_announce.pack)


tapis.contree_window.mainloop()
tapis.contree_window.destroy()
