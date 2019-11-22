
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 08:58:58 2019

@author: ludodata
"""
import random
import pandas
from tkinter import *
from PIL import ImageTk, Image
import os


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
    nextDuo = Button(mainWindow, text = "Afficher la liste aléatoire", fg="red", command = fetekdo)
    nextDuo.pack(side = TOP, ipadx = 40, padx = 40, ipady = 20, pady = 40)
    choiceMenu1.pack_forget()
    choiceMenu2.pack_forget()

def readme():
    wReadme = Toplevel(mainWindow)

mainWindow = Tk()
img = ImageTk.PhotoImage(master = mainWindow, file="kdo.gif")
panel = Label(mainWindow, image = img)
panel.pack(side = "left", fill = "both", expand = "yes")

mainWindow.title('FETEKDO')

choiceMenu1 = Button(mainWindow, text = "FETEKDO", fg="red", command = funFetekdo)
choiceMenu1.pack(side = TOP, ipadx = 20, padx = 60, ipady = 25, pady = 25)
choiceMenu2 = Button(mainWindow, text = "Choisir Fichier", fg="red", command = readme)
choiceMenu2.pack(side = TOP, ipadx = 20, padx = 60, ipady = 25, pady = 25)
choiceMenu3 = Button(mainWindow, text = "Quitter", fg="black", command = mainWindow.destroy)
choiceMenu3.pack(side = TOP, ipadx = 20, padx = 60, ipady = 25, pady = 15)

mainWindow.mainloop()