# coding: utf8

from tkinter import *

#but = Button(frame, height = 5, width = 10, command = "", )
class card_button(object):

    def __init__(self, frame_winfow, command, image, height=5, width=10):
        self.button = Button(frame_winfow, height=height, width=width, command=command)
        self.button.grid()


class announcement_button(object):
    
    def __init__(self, frame, text, item, variable, row, column):
        self.button = Radiobutton(frame, text=text, value=item, variable=variable, height=1, width=10, fg="blue")
        self.button.grid(row=row, column=column)


class announcement_value_button(announcement_button):

    def __init__(self, frame, value, column, variable):
        super().__init__(frame)
        self.button.configure(text=value, value=value, variable=variable, row=0, column=column)
 


class announcement_color_button(announcement_button):

    def __init__(self, frame, color, column, variable):
        super().__init__(frame)
        self.button.configure(text=color, value=color, variable=variable, row=1, column=column)
     #   self.button.rowconfigure(1)
     #   self.button.columnconfigure(column)