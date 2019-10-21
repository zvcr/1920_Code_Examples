# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 13:21:12 2019

@author: D. Bergmans
"""

# Gebruiker vragen om 2 getallen
getal1 = input("Geef getal 1:")
getal2 = input("Geef getal 2:")

# Ingevoerd getal omzetten naar een int
getal1 = int(getal1)
getal2 = int(getal2)

# De 2 getallen optellen en opslaan in de variable uitkomst
uitkomst = getal1+getal2

# De uitkomst op het scherm tonen
print("De uitkomst is",uitkomst)

# Afhankelijk van de uitkomst hoger, lager of precies tonen
if uitkomst > 10:
    print("Hoger")

if uitkomst < 10:
    print("Lager")

if uitkomst == 10:
    print("Precies")
    
# Gebruiker vragen om plus of min sommen
keuze = input("Wilt u plus of min sommen oefenen?")

# Als de gebruiker 'plus' heeft ingevoerd
if keuze == "plus":
    print("U heeft gekozen voor plussommen!")

# Als de gebruiker 'min' heeft ingevoerd
if keuze == "min":
    print("U heeft gekozen voor minsommen")