import random
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
#show my cards
# place bets  
#draw 2 cards to each player 
#ask of play would like to "stand" or "hit"
# dray two cards to dealer (one face down)
#check if card count is 21
    #if card count for players is 21 then blackjack, dealer pays player one and half times amount of their bet 
    #if dealer card count is 21 then collects all bets who dont have 21
    #if dealer and player have 21 then "tie"
    #if not then keep playing till 21

class CardBoard():
    CARDS = ["2", "3", "4", "5", "6", "7", "8","9" ,"J" ,"K" ,"Q" ,"A"]*4
        
    def __init__(self):
        self.card = random.shuffle(CardBoard)
        self.cards = CardBoard
        self.solved = False
        

    def show_card(self):    
        deck = self.card.pop()
        if deck == "J": deck == 10
        if deck == "K": deck ==10
        if deck == "Q": deck ==10
        if deck == "A": deck == 1 or deck == 11


    def card_count(self): 
        hand =[]
        dealer_hand = []
        total_hand = []
        for card in hand and dealer_hand:
            if card == "2": 
                total_hand += 2
            if card == "3":
                total_hand +=3
            if card == "4":
                total_hand +=4
            if card == "5":
                total_hand +=5
            if card == "6":
                total_hand +=6
            if card == "7":
                total_hand +=7
            if card == "8":
                total_hand +=8
            if card == "9":
                total_hand +=9
            if card == "J":
                total_hand +=10
            if card == "K":
                total_hand +=10
            if card == "Q":
                total_hand +=10
            if card == "A":
                response_A = input ("Would you like to add 1 or 11?")
                if response_A == "1":
                    total_hand += 1
                    return total_hand
                else:
                    total_hand += 11
                    return total_hand
                                 
       
    def take_hit(self): 
        self.dealers_hand += self.cards * 2
        self.players_hand += self.cards * 2

    def take_stand(self):
        return self.card_count

    def dealers_hand(self):
        for card in self.card:
            dealers_hand = card.append()

    def player_hand(self):
        for card in self.card:
            players_hand = card.append()



class UI(): 
    def __init__(self): 
        self.card_board = CardBoard()

    def play_game(self):
        print("Welcome to BLACKJACK!")
        while not self.card_board.solved:
            self.card_board.take_hit
            self.card_board.card_count
            card = input("Would you like to hit or stand")
            if card.lower() == "hit":
                self.card_board.take_hit
            else:
                self.card_board.take_stand
        for card in self.dealer_hand:
            if self.dealer_hand >= 21:
                print("Blackjack")
            if self.player_hand >= 21:
                print("BlackJack")


ui = UI()
ui.play_game           


            
            

                

            

        




