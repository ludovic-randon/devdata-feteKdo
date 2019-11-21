
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 08:58:58 2019

@author: ludodata
"""
import random
import pandas
from tkinter import *


def readme():
    wReadme = Toplevel(mainWindow)

def fetekdo():
    df = pandas.read_csv('names.csv')
    list_csv = df.values.tolist()
    list = []
    for i in list_csv:
        list = list+i
    random.shuffle(list)
    duo_sort = Label(text = 'Le premier : ')
    duo_sort.pack()
    for i in list:
        duo_sort = Label(text = i + ' donne à :')
        duo_sort.pack()
    duo_sort = Label(text = list[0] + ', fin de la liste !')
    duo_sort.pack()

def funFetekdo():
    nextDuo = Button(mainWindow, text = "Afficher le duo suivant", command = fetekdo)
    nextDuo.pack(side = TOP, ipadx = 40, padx = 30, ipady = 20, pady = 20)
    choiceMenu1.pack_forget()
    choiceMenu2.pack_forget()



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