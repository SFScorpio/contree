# coding: utf8

from tkinter import *
from class_player import *


def choose_game(lstplayer):
    choose_game_window = Tk()
    
    choose_game_label = Label(choose_game_window, text = "Wich game do you wanna play?").grid(row = 1)
    contree_button = Button(choose_game_window, text = "Contree", command = lambda: def_contree_players(choose_game_window, lstplayer))
    contree_button.grid(row = 2)
    
    choose_game_window.mainloop()


def def_contree_players(window, lstplayer):
    window.destroy()
    
    player_number = 4
    nplayer = 1
    lstentry = []
    name_window = Tk()
    
    for num in range(player_number):
        entrynum = "entry" + str(num)
        
        num = Label(name_window, text = "player name " + str(nplayer)).grid(column = 1, row = nplayer)
        entrynum = Entry(name_window)
        entrynum.grid(column = 2, row = nplayer)
        nplayer += 1
        lstentry += [entrynum]
        
    start_button = Button(name_window, text = "start", command = lambda: create_players(lstentry, name_window, lstplayer))
    start_button.grid(column = 2, row = nplayer)
    
    name_window.mainloop()


def create_players(lstentry, window2, lstplayer):
    for player_name in lstentry:
        print("coucou")
        gplayer = player()
        gplayer.name = player_name.get()
        lstplayer += [gplayer]
    print(type(lstplayer), len(lstplayer))
    return lstplayer, window2.destroy()
