import tkinter
from tkinter import *
import random
import sys

class Player:
    
    def __init__(self,name):
        self.name = name
        self.hand =[]

    def Start():
        for x in range (0,2):
            # Deletes one card from the end of the deck and puts it in the player hand
            self.hand.append(deck.pop())
            # Same but for the computer

deck=["A","A","A","A",2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,"J","J","J","J","Q","Q","Q","Q","K","K","K","K"]
random.shuffle(deck)

    
