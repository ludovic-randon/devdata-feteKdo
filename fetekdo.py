#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 08:58:58 2019

@author: ludodata
"""

import function as func
from tkinter import *

def funFetekdo():
    wFetekdo = Toplevel(mainWindow)
    nextDuo = Button(wFetekdo, text = "Afficher le duo suivant", command = func.fetekdo)
    nextDuo.pack(side = TOP, ipadx = 40, padx = 30, ipady = 20, pady = 20)


def readme():
    wReadme = Toplevel(mainWindow)

mainWindow = Tk()
choiceMenu1 = Button(mainWindow, text = "FETEKDO", command = funFetekdo)
choiceMenu1.pack(side = TOP, ipadx = 20, padx = 20, ipady = 25, pady = 25)
choiceMenu2 = Button(mainWindow, text = "ReadMe", command = readme)
choiceMenu2.pack(side = TOP, ipadx = 20, padx = 20, ipady = 25, pady = 25)
choiceMenu3 = Button(mainWindow, text = "Quitter", command = mainWindow.destroy)
choiceMenu3.pack(side = TOP, ipadx = 20, padx = 20, ipady = 25, pady = 25)
mainWindow.mainloop()
