import sys
import random

class Card:
    suit = ['♥', '♦', '♣', '♠']
    value = {'A':11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        
class BlackjackGame:
    def __init__(self):
        self.deck = []
        self.player_hand = [] 
        self.dealer_hand = [] 
        
    def main(self):
        print('\n\nRules:\n Try to get as close to 21 without going over\n Kings, Queens and Jacks are worth 10 points.\n Aces are worth 1 or 11 points.\n Cards 2 through 10 are worth their face value.\n (H)it to take another card.\n (S)tand to stop taking cards.\n  On your first play, you can (D)ouble down to increase your bet\n  but must hit exactly one more time before standing.\n  In case of a tie, the bet is returned to the player.\n  The dealer stops hitting at 17.')
        money_input = int(input('Money: '))
        self.build_card()
        self.bet_input = input(f'How much do you bet? (1-{money_input}, or QUIT) ')
        if self.bet_input.upper() == 'QUIT':
            print('Goodbye')
            sys.exit()
        else:
            self.bet_input = int(self.bet_input)
            print(f'Bet: {self.bet_input}')
            print()
            random.shuffle(self.deck)
            self.dealer_hand.append(self.deck.pop())
            self.dealer_hand.append(self.deck.pop())
            self.player_hand.append(self.deck.pop())
            self.player_hand.append(self.deck.pop())  
            self.dealer()
            self.player()
            self.action()
            
    def dealer(self):  
        print('DEALER: ???\n') 
        self.show_dealers_hand()
        print()
            
    def player(self):
        self.player_count = 0
        for card in self.player_hand:
            actual_value = Card.value[card.value]
            self.player_count += actual_value
        print(f'PLAYER: {self.player_count}')
        self.show_players_hand()
            
    def build_card(self):
        for suit in Card.suit:
            for value in Card.value:
                self.deck.append(Card(suit,value))

    def show_dealers_hand(self):
        rows = ['', '', '', '']
        first = True
        
        for card in self.dealer_hand:
            suit = card.suit
            value = card.value
            if first == True:
                rows[0] += (' ___ ')
                rows[1] += ('|## |')
                rows[2] += ('|###|')
                rows[3] += ('|_##|')
                first = False
            else:
                suit = card.suit
                value = card.value
                rows[0] += ' ___ ' 
                rows[1] += f'|{value} |' 
                rows[2] += f'| {suit}| ' 
                rows[3] += f'|__{value}|' 
        for row in rows:
            print(row)

    def show_players_hand(self):
        rows = ['', '', '', '']
        
        for card in self.player_hand:
            suit = card.suit
            value = card.value
            rows[0] += ' ___ ' 
            rows[1] += f'|{value} |' 
            rows[2] += f'| {suit}| ' 
            rows[3] += f'|__{value}|' 
        for row in rows:
            print(row)
            
    def action(self):
        print()
                
        new_action = input('(H)it, (S)tand, (D)ouble down ')
        
        if new_action.lower() == 'h':
            new_card = self.deck.pop()
            self.player_hand.append(new_card) 
            self.dealer_hand.append(self.deck.pop())
            print(f'You drew a {new_card.value} of {new_card.suit}. ')
            print()
            
        elif new_action.lower() == 's':
            print('You chose to stand')
            print()
            pass 
        
        elif new_action.lower() == 'd':
            self.bet_input = self.bet_input * 2
            new_card = self.deck.pop()
            self.player_hand.append(new_card)    
            print(f'You doubled down and drew a {new_card.value} of {new_card.suit}.')
            current_dealer_score = 0
            for card in self.dealer_hand:
                current_dealer_score += Card.value[card.value]
            if current_dealer_score < 17:
                self.dealer_hand.append(self.deck.pop())
            
        self.reveal_dealer()
        self.reveal_player()  
        self.game_decision()
            
    def reveal_dealer(self):
        self.dealer_count = 0
        for card in self.dealer_hand:
            actual_value = Card.value[card.value]
            self.dealer_count += actual_value
        print(f'DEALER: {self.dealer_count}')
        print()
        rows = ['', '', '', '']
        for card in self.dealer_hand:
            suit = card.suit
            value = card.value 
            rows[0] += ' ___ ' 
            rows[1] += f'|{value} |' 
            rows[2] += f'| {suit}| ' 
            rows[3] += f'|__{value}|'   
        for row in rows:
            print(row)
        print()
        
    def reveal_player(self):
        self.player_count = 0
        for card in self.player_hand:
            actual_value = Card.value[card.value]
            self.player_count += actual_value
        print(f'PLAYER: {self.player_count}')  
        print()
        
        rows = ['', '', '', '']
        for card in self.player_hand:
            suit = card.suit
            value = card.value 
            rows[0] += ' ___ ' 
            rows[1] += f'|{value} |' 
            rows[2] += f'| {suit}| ' 
            rows[3] += f'|__{value}|'   
        for row in rows:
            print(row)
        print()

    def game_decision(self):
        if self.player_count > self.dealer_count and self.player_count <= 21:
            print(f'You won ${self.bet_input} dollars!')
            print()
            
        elif self.player_count > self.dealer_count and self.player_count <= 21 and new_action.lower() == 'd':
            print(f'You won ${self.bet_input * 2} dollars!')
            print()            
        else:
            print('You lost')
            print()

game = BlackjackGame()
game.main()