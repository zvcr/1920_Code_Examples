# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 08:54:41 2019

@author: D. Bergmans
"""
def menu():
    lengte = input("Voer de lengte in: ")
    breedte = input("Voer de breedte in: ")
    
    lengte = int(lengte)
    breedte = int(breedte)
    
    berekenOppervlakte(lengte,breedte)

def berekenOppervlakte(x,y):
    oppervlakte = x*y
    print("Oppervlakte",oppervlakte)
    
    keuze = input("Wilt u nog een berekening maken?")
    if keuze == "j":
        menu()
    else:
        print("Bedankt en tot ziens!")
    
menu()