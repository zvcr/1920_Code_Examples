# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 14:33:30 2019

@author: D. Bergmans
"""

def menu():
    print("U heeft de volgende opties: [b]estellen, [t]onen, [p]rijs, [a]fsluiten")
    keuze = input("Maak uw keuze: ")
    if keuze == "b":
        maakBestelling()
    elif keuze == "t":
        geefBestellingen()
    elif keuze == "p":
        geefTotaalPrijs()
    elif keuze == "a":
        print("Bedankt en tot ziens")
    else:
        print(keuze,"is geen geldige keuze")
        menu()

def maakBestelling():
    print("Hier kunt u later uw bestelling maken")
    menu()

def geefBestellingen():
    print("Hier komen de bestellingen")
    menu()

def geefTotaalPrijs():
    print("Hier komt de totaalprijs")
    menu()

menu()