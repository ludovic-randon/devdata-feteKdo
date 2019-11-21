
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 08:58:58 2019

@author: ludodata
"""

import function as func


choiceMenu = input("Menu:\n\n 1. FETEKDO\n\n 2. ReadMe\n\n 3. Quitter \n\n")

while choiceMenu == "1" or "2":
    if choiceMenu == "1":
        func.fetekdo()
        choiceMenu = input("Menu:\n\n 1. FETEKDO\n\n 2. ReadMe\n\n 3. Quitter \n")

    elif choiceMenu == "2":
        print("REEEAAAADMEEE")
        choiceMenu = input("Menu:\n\n 1. FETEKDO\n\n 2. ReadMe\n\n 3. Quitter \n")

    else: 
        break
