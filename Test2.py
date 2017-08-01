import tkinter
from tkinter import *
import random
import sys

split = False
# This is for a GUI which has buttons
class Game(tkinter.Tk):
    # Creates a the window 
    def __init__(self):
        tkinter.Tk.__init__(self)
        # Name of the window
        self.title("BlackJack")

        global Visual
        Visual = Listbox()
        Visual.pack(fill=tkinter.BOTH, expand=0)
        
        # Creates the button for start
        button = tkinter.Button(text="Start", command=self.Start)
        button.pack(fill=tkinter.BOTH, expand=0)
        # Creates the button for hit
        button = tkinter.Button(text="Hit", command=self.Hit)
        button.pack(fill=tkinter.BOTH, expand=0)
        # Creates the button for split
        button = tkinter.Button(text="Split", command=self.Split)
        button.pack(fill=tkinter.BOTH, expand=0)
        # Creates the button for stand
        button = tkinter.Button(text="Stand", command=self.Stand)
        button.pack(fill=tkinter.BOTH, expand=0)



    # Reset/ Start the game 
    def Start(self):
        print("START")
        global pscore
        global cscore
        global player
        global computer
        global deck
        global player2
        global split
        # pscore is player score 
        pscore = 0
        # cscore is computer score 
        cscore = 0
        #player is  player hand  
        player=[]
        #player2 is second player hand in case of split 
        player2=[]
        #computer is  player hand 
        computer=[]
        # Full 52 card deck 
        deck=["A","A","A","A",2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,"J","J","J","J","Q","Q","Q","Q","K","K","K","K"]
        # Shuffles the deck randomly 
        random.shuffle(deck)
        #Gives inital cards 
        for x in range (0,2):
            # Deletes one card from the end of the deck and puts it in the player hand
            player.append(deck.pop())
            # Same but for the computer
            computer.append(deck.pop())
        # One of the "dealer's" card needs to be shown 
        print ("This is one of your opponent's cards: " + str(computer[0]))
        print ("This is your deck " + str(player))
        score()

    # Get one card 
    def Hit(self):
        global split
        print("HIT")
        #Deletes one card from the end of the deck and puts it in the player hand
        player.append(deck.pop())
        # When the player uses the split function draws a card for the other hand
        if split == True:
            player2.append(deck.pop())
        #Computer will keep drawing cards if it has less than 16 in score or has 5 cards drawn
        while cscore <= 16 and len(computer) != 5:
            computer.append(deck.pop())
            # Checks the score so the cscore is calculated each time a new card is added
            score()
        # Checks the score for player 
        score()
        # If the players cant draw anymore cards it automatically ends the gameb
        if len(player) == 5 and len(computer) == 5:
            Stand()
    # Ends the game 
    def Stand(self):
        global cscore
        global pscore
        global split
        print("STAND")
        print("This is your deck " + str(player))
        if split == True:
            print("This is your other deck " + str(player2))
        #Computer will keep drawing cards if it has less than 16 in score or has 5 cards drawn
        while cscore <= 16 and len(computer) != 5:
            computer.append(deck.pop())
            score()
 
        score()
        Visual.insert(END,"This is your opponent's deck " + str(computer))
        # Compares the score and declares the winner
        if pscore == cscore and len(computer) == len(player):
            Visual.insert(END,"DRAW")
        elif pscore == cscore and len(computer) > len(player):
            Visual.insert(END,"VICTORY")
        elif pscore == cscore and len(player) > len(computer):
            Visual.insert(END,"LOSE") 
        elif pscore > cscore and pscore ==21:
            Visual.insert(END,"BLACKJACK")
        elif pscore > cscore:
            Visual.insert(END,"VICTORY")
            sys.exit("You have won as your score is greater than computer score")
        elif pscore < cscore:
            Visual.insert(END,"LOSE")
            sys.exit("You have won as computer score is greater than your score")
               

    # Calculates the current score
    global score
    def score():
        global cscore
        global pscore
        # Resets the score whenever recalculating
        pscore = 0
        cscore = 0
        # Calculate player score
        # This sets it so it repeats the same length as the hand
        for x in range(0,len(player)):
            # Sets all the Royals as 10 
            if player[x] == "J" or player[x] == "Q" or player[x] == "K":
                pscore = pscore + 10
                
            # Sets Ace to 11 or 1 
            elif player[x] == "A":
                pscore = pscore + 11
                # If it is over 21 it sets ace worth to 1
                if pscore > 21:
                    pscore = pscore - 10
            # Other normal cards are already integers so just add to pscore
            else:
                pscore = pscore + player[x]
        # Same as player but for the computer
        for x in range(0,len(computer)):
            if computer[x] == "J" or computer[x] == "Q" or computer[x] == "K":
                cscore = cscore + 10
            elif computer[x] == "A":
                cscore = cscore + 11
                if cscore > 21:
                    cscore = cscore - 10
            else:
                cscore = cscore + computer[x]
        # prints player deck 
        print("This is your deck " + str(player))
        print(pscore)
        List()

        

    def Split(self):
        global player
        global pscore
        global player2
        if player[0] == "J" or player[0] == "Q" or player[0] == 10 or player[0] == "K" and player[1] == "K" or player[1] == "Q" or player[1] == "J" or player[1] == 10  and pscore == 20:
            player2.append(player[1])
            player.remove(player2[0])
            split = True

    global List
    def List():
        global Visual
        global player
        Visual.delete(0, tkinter.END)
        Visual.insert(END,"This is your deck " + str(player))
        Visual.insert(END,"This is your score " + str(pscore))
        Visual.update_idletasks()
        #Bust conditions for both player and computer while betting 
        if pscore > 21:
            Visual.insert(END,"This is your opponent's deck " + str(computer))
            Visual.insert(END,"BUST")
            sys.exit("You have lost as your score is greater than 21")
        elif cscore > 21:
            Visual.insert(END,"This is your opponent's deck " + str(computer))
            Visual.insert(END,"VICTORY")
            sys.exit("You have won as computer score is greater than 21")

if __name__ == "__main__":
    application = Game()
    application.mainloop()






