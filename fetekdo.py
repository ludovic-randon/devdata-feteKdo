
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 08:58:58 2019

@author: ludodata
"""
import random
import pandas
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
import shutil

new_list = []

def resetList():
    global new_list
    new_list = []
    
# Fonction pour selectionner le fichier souhaité a passer en liste et le copier dans le rep courant
def addList():
    global new_list
    file_convert = shutil.copy2(filedialog.askopenfilename(), '../FeteKDO-Project/list_regist')
    # fichiers csv ou xlsx
    if file_convert.endswith('.csv') or file_convert.endswith('.xlsx'):
        df = pandas.read_csv(file_convert)
        # On passe le csv lu dans une variable sous forme de liste
        list_csv = df.values.tolist()
        # Pour les fichiers csv qui ont des liste dans une liste, on concatène les listes
        for i in list_csv:
            new_list = new_list+i
    # fichiers txt
    if file_convert.endswith('.txt'):
        df = pandas.read_csv(file_convert, sep="\n", header=None)
        # On passe le csv lu dans une variable sous forme de liste
        list_csv = df.values.tolist()
        # Pour les fichiers csv qui ont des liste dans une liste, on concatène les listes
        for i in list_csv:
            new_list = new_list+i
    # Mélange de la liste pour un affichage rand
    for i in os.listdir("list_regist"):
        os.remove("list_regist/" + i)
    return new_list

def delete():
    for i in os.listdir("list_regist"):
        os.remove("list_regist/" + i)
    
# Fonction principale, lecture de fichier et affichage rand de la liste contenue
def fetekdo():
    global new_list
    list_clean = new_list
    random.shuffle(list_clean)
    # Affichage de la liste
    for i in list_clean:
        i = str(i)
        duo_sort.insert(END, i + ' donne à :')
    # Affichage du dernier de la liste à recevoir (premier à donner)
    duo_sort.insert(END, list_clean[0] + ', fin de la liste !')

# Fonction qui passe du menu principal au menu d'exe de la func principale
def funFetekdo():
    nextDuo = Button(mainWindow, text = "Afficher la liste aléatoire", fg="red", command = fetekdo)
    nextDuo.pack(side = TOP, ipadx = 40, padx = 40, ipady = 20, pady = 40)
    choiceMenu1.pack_forget()
    choiceMenu2.pack_forget()
    choiceDelete.pack_forget()
    duo_sort.pack(side = BOTTOM)

# Déclaration de la fenêtre principale et design de celle ci + scrollbar
mainWindow = Tk()
img = ImageTk.PhotoImage(master = mainWindow, file="kdo.gif")
panel = Label(mainWindow, image = img)
panel.pack(side = "left", fill = "both", expand = "yes")
scrollbar = Scrollbar(mainWindow)
scrollbar.pack(side = RIGHT, fill = Y)
# Déclaration de la listbox mais unpack (cf: def funFetekdo():)
duo_sort = Listbox(mainWindow, bd=0, yscrollcommand = scrollbar.set, height = 20, width = 45)

# Nom de la fenêtre / Appli
mainWindow.title('FETEKDO')

# Déclaration et affichage des boutons du 'menu principal'
choiceMenu1 = Button(mainWindow, text = "FETEKDO", fg="red", command = funFetekdo)
choiceMenu1.pack(side = TOP, ipadx = 20, padx = 60, ipady = 25, pady = 25)
choiceMenu2 = Button(mainWindow, text = "Ajouter une liste", fg="red", command = addList)
choiceMenu2.pack(side = TOP, ipadx = 20, padx = 60, ipady = 25, pady = 10)
choiceDelete = Button(mainWindow, text = "Réinitialiser les listes ?", fg="red", command = resetList)
choiceDelete.pack(side = TOP, ipadx = 20, padx = 60, ipady = 25, pady = 10)
choiceMenu3 = Button(mainWindow, text = "Quitter", fg="black", command = mainWindow.destroy)
choiceMenu3.pack(side = TOP, ipadx = 20, padx = 60, ipady = 25, pady = 15)

mainWindow.mainloop()