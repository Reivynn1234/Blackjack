import tkinter
import random
import sys

class Game(tkinter.Tk):
    
    def __init__(self):
        tkinter.Tk.__init__(self)
        self.title("BlackJack")
        
        button = tkinter.Button(text="Start", command=self.Start)
        button.pack(fill=tkinter.BOTH, expand=0)
        
        button = tkinter.Button(text="Hit", command=self.Hit)
        button.pack(fill=tkinter.BOTH, expand=0)

        button = tkinter.Button(text="Stand", command=self.Stand)
        button.pack(fill=tkinter.BOTH, expand=0)

    # Reset/ Start the game 
    def Start(self):
        global pscore
        global hP
        global hC
        global cscore
        global player
        global computer
        global deck
        global player2
        global hP2
        # pscore is player score 
        pscore = 0
        #hP is hand counter for player
        hP = 2
        #hP 2 is hand counter for a player 
        hP2 = 1
        # hC is hand counter for the computer
        hC = 2
        # cscore is computer score 
        cscore = 0
        #player is  player hand *5 for the length 
        player=[0]*5
        #player2 is second player hand in case of split *5 for the length
        player2=[0]*5
        #computer is  player hand *5 for the length 
        computer=[0]*5
        # Full 52 card deck 
        deck=["A","A","A","A",2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,"J","J","J","J","Q","Q","Q","Q","K","K","K","K"]
        # Shuffles the deck randomly 
        random.shuffle(deck)
        #Gives inital cards 
        for x in range (0,2):
            # Deletes one card from the end of the deck and puts it in the player hand
            player[x]=deck.pop()
            # Same but for the computer
            computer[x]=deck.pop()
        # One of the "dealer's" card needs to be shown 
        print ("This is one of your opponent's cards: " + str(computer[0]))
        print ("This is your deck " + str(player))
        score()

    # Get one card 
    def Hit(self):
        global score
        global hC
        global hP
        #Deletes one card from the end of the deck and puts it in the player hand
        player[hP]=deck.pop()
        #Computer will keep drawing cards if it has less than 16 in score or has 5 cards drawn
        while cscore <= 16 or computer[4] != 0:
            computer[hC]=deck.pop()
            score()
            hC = hC + 1
        hP = hP + 1
        score()
        if player[4] != 0 and computer[4] != 0:
            end()
        
    def Stand(self):
        global score
        global hP
        global hC
        global cscore
        global pscore
        print("This is your deck " + str(player))
        #Computer will keep drawing cards if it has less than 16 in score or has 5 cards drawn
        while cscore <= 16 or computer[4] != 0:
            computer[hC]=deck.pop()
            score()
            hC = hC + 1
        print("This is your opponent's deck " + str(computer))
        score()
        # Compares the score and declares the winner
        if pscore > cscore and pscore ==21:
            print("BLACKJACK")
        elif pscore > cscore:
            print("VICTORY")
            sys.exit("You have won as your score is greater than computer score")
        elif pscore > cscore:
            print("LOSE")
            sys.exit("You have won as computer score is greater than your score")
        elif pscore == cscore and hC == hP:
            print("DRAW")
        elif pscore == cscore and hC > hP:
            print("VICTORY")
        elif pscore == cscore and hP > hC:
            print("LOSE")        

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
                
            # Sets Ace to 11 or 10 
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
        #Bust conditions for both player and computer while betting 
        if pscore > 21:
            print("This is your opponent's deck " + str(computer))
            print("BUST")
            sys.exit("You have lost as your score is greater than 21")
        elif cscore > 21:
            print("This is your opponent's deck " + str(computer))
            print("VICTORY")
            sys.exit("You have won as computer score is greater than 21")

if __name__ == "__main__":
    application = Game()
    application.mainloop()






