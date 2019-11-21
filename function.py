#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 08:58:25 2019

@author: ludodata
"""

import random
import pandas
from tkinter import *

def fetekdo():
    df = pandas.read_csv('/home/utilisateur/Documents/projets/FeteKDO-Project/names.csv')
    list_csv = df.values.tolist()
        
    list = []
    for i in list_csv:
        list = list+i
    
    random.shuffle(list)

    i=0

    while i != len(list):
        index_max = len(list) - 1
        continue_sort = input('Tirer le duo suivant ? O/N ')
        if continue_sort.lower() == 'o':
            if i < index_max:
                print(list[i], ' donne à ', list[i+1])
                i = i + 1
            else:
                print(list[len(list) - 1], ' donne à ', list[0])
                break
        elif continue_sort.lower() == 'n':
            print('Salut, à la prochaine !')
            break
        else:
            print("Lettre 'O' ou lettre 'N' !")
