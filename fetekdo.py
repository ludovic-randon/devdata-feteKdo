
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 08:58:58 2019

@author: Ejhb, Bobba Ash, Dysdylan, Ludo-R
"""
import random
import pandas
from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
import os
import shutil
import pygame

pygame.mixer.init()
pygame.mixer.music.load("hihi.wav")
pygame.mixer.music.play()
# Boolean music est en lecture 
music_playing = True 

new_list = []

# Fonction on/off music 
def playstop():
    global music_playing
    if music_playing == True:
        pygame.mixer.music.pause()
        music_playing = False
        choiceMusic.config(bg = "#d10b10")
    else:
        pygame.mixer.music.unpause()
        music_playing = True
        choiceMusic.config(bg = "green")
#Fonction qui coupe la music et coupe l'application.
def windowQuit():
    pygame.mixer.music.pause()
    mainWindow.destroy()
        

# Fonction de reset de la var new_list en liste vide
def resetList():
    global new_list
    new_list = []
    
# Fonction pour selectionner le fichier souhaité a passer en liste 
def addList():
    global new_list
    file_convert = filedialog.askopenfilename()
    # convert fichiers csv ou xlsx
    if file_convert.endswith('.csv') or file_convert.endswith('.xlsx'):
        df = pandas.read_csv(file_convert)
        list_csv = df.values.tolist()
        for i in list_csv:
            new_list = new_list+i
    # convert fichiers txt
    if file_convert.endswith('.txt'):
        df = pandas.read_csv(file_convert, sep="\n", header=None)
        list_csv = df.values.tolist()
        for i in list_csv:
            new_list = new_list+i
    # Mélange de la liste pour un affichage rand
    random.shuffle(new_list)
    return new_list

count = 0
# Fonction principale, lecture de fichier et affichage rand de la liste contenue
def fetekdo():
    global new_list
    global count
    # Affichage de la liste
    if count < len(new_list) - 1:
        duo_sort.insert(END, str(new_list[count]) + ' donne à ' + str(new_list[count+1]))
        count = count + 1
    else:
        # Affichage du dernier de la liste à recevoir (premier à donner)
        duo_sort.insert(END, str(new_list[len(new_list)-1]) + ' donne à ' + str(new_list[0]))
        duo_sort.insert(END, '!!! FIN DE LISTE !!!')
        count = 0
        random.shuffle(new_list)

# Fonction qui passe du menu principal au menu d'exe de la func principale
def funFetekdo():
    choiceMenu3.pack_forget()
    choiceMenu3.pack(side = RIGHT, ipadx = 20, padx = 20, ipady = 25, pady = 15)
    buttonBack.pack(side = LEFT, ipadx = 20, padx = 20, ipady = 25, pady = 15)
    nextDuo.pack(side = TOP, ipadx = 60, padx = 10, ipady = 60, pady = 20)
    choiceMusic.pack(side = LEFT, ipadx = 20, padx = 60, ipady = 25, pady = 15)
    choiceMenu1.pack_forget()
    choiceMenu2.pack_forget()
    choiceDelete.pack_forget()
    duo_sort.pack(side = BOTTOM)

# Bouton de retour, on désaffiche les boutons et la liste et réaffiche ceux du menu
def backMenu():
    choiceMenu1.pack(side = TOP, ipadx = 20, padx = 60, ipady = 25, pady = 25)
    choiceMenu2.pack(side = TOP, ipadx = 20, padx = 60, ipady = 25, pady = 10)
    choiceDelete.pack(side = TOP, ipadx = 20, padx = 60, ipady = 25, pady = 10)
    choiceMenu3.pack_forget()
    choiceMenu3.pack(side = RIGHT, ipadx = 20, padx = 60, ipady = 25, pady = 15)
    nextDuo.pack_forget()
    choiceMusic.pack_forget()
    choiceMusic.pack(side = LEFT, ipadx = 20, padx = 60, ipady = 25, pady = 15)
    duo_sort.delete(0, END)
    duo_sort.pack_forget()
    buttonBack.pack_forget()

# Déclaration de la fenêtre principale et design de celle ci + scrollbar
mainWindow = Tk()
img = ImageTk.PhotoImage(master = mainWindow, file="kdo.gif")
panel = Label(mainWindow, image = img)
panel.pack(side = "left", fill = "both", expand = "yes")
scrollbar = Scrollbar(mainWindow)
scrollbar.pack(side = RIGHT, fill = Y)

# Déclaration de la listbox mais unpack (cf: def funFetekdo():)
duo_sort = Listbox(mainWindow, font=('calibri', 13, 'bold'), bd=0, yscrollcommand = scrollbar.set, height = 30, width = 80)

# Déclaration bouton de retour
buttonBack = Button(mainWindow, text= "Retour", font=('calibri', 13, 'bold', 'underline'), bg='#07d800', fg='black', bd=8, command = backMenu)

# Déclaration bouton pour afficher le shuffle liste
nextDuo = Button(mainWindow, text = "Afficher le duo suivant :", font=('calibri', 13, 'bold', 'underline'), bg='#661aff', fg='black', bd=8, command = fetekdo)

# Nom de la fenêtre / Appli
mainWindow.title('FETEKDO')

# Déclaration et affichage des boutons du 'menu principal'
choiceMenu1 = Button(mainWindow, text = "FETEKDO", bg='#ffcc00', font=('calibri', 13, 'bold', 'underline'), fg='black', bd=8, command = funFetekdo)
choiceMenu1.pack(side = TOP, ipadx = 20, padx = 60, ipady = 25, pady = 25)
choiceMenu2 = Button(mainWindow, text = "Ajouter une liste", bg='#10d10b', font=('calibri', 12, 'bold'), fg='black', bd=8, command = addList)
choiceMenu2.pack(side = TOP, ipadx = 20, padx = 60, ipady = 25, pady = 10)
choiceDelete = Button(mainWindow, text = "Réinitialiser les listes ?", bg='#ea8f04', font=('calibri', 12, 'bold'), fg='black', bd=8, command = resetList)
choiceDelete.pack(side = TOP, ipadx = 20, padx = 60, ipady = 25, pady = 10)
choiceMenu3 = Button(mainWindow, text = "Quitter", bg='#d10b10', font=('calibri', 11, 'bold', 'underline'), fg='black', bd=8, command = windowQuit)
choiceMenu3.pack(side = RIGHT, ipadx = 20, padx = 60, ipady = 25, pady = 15)
# Déclaration du bouton music 
choiceMusic = Button(mainWindow, text = "Play/Stop", bg='green', font=('calibri', 9, 'bold', 'underline'), fg='black', bd=8, command = playstop)
choiceMusic.pack(side = LEFT, ipadx = 20, padx = 60, ipady = 25, pady = 15)




mainWindow.mainloop()