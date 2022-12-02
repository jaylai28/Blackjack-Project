############ Libraries #########
import random
from art import logo
import os
############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:

## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)
    
def player_turn(player_list):
    player_list.append(deal_cards())
    
def dealer_turn(dealer_list):
    dealer_list.append(deal_cards())

def compare_result(player_score, dealer_score):
    """
    This function compares the player and dealer score and determine the winner.
    """
    if player_score == dealer_score:
        return "Draw 🙃"

    if player_score == 21:
        return "Win with a Blackjack 😎"

    if player_score > 21 and dealer_score > 21:
        return "You went over. You lose 😤"

    if player_score > 21:
        return "You went over. You lose 😭"

    if dealer_score == 21:
        return "Lose, opponent has Blackjack 😱"

    if dealer_score > 21:
        return "Opponent went over. You win 😁"
    
    if player_score > dealer_score and player_score <= 21:
        return "You win 😃"

    else:
        return "You lose 😤"
        
end_of_game = False
#Keep playing the game when the game is not ending
while not end_of_game:
    u_input = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    first_flag = False
    player_list=[]
    dealer_list=[]
    #End the game if the user input is 'n'
    if u_input == 'n':
        end_of_game = True
    #Allow the player to draw cards each turn
    while u_input != 'n':
        #Serve the card to both player and dealer during the first turn
        if first_flag == False:
            #Clear the screen & print the Blackjack logo every new game
            os.system('clear')
            print(logo)
            #Serve card to player and dealer during the first turn
            player_turn(player_list)
            dealer_turn(dealer_list)
            #Get the score for the player and dealer
            player_score = sum(player_list)
            dealer_score = sum(dealer_list)

            print(f"Your cards: {player_list}, current score: {player_score}\nComputer's first card: {dealer_list}")
            first_flag = True
        
        if player_score <= 21:
            get_card = input("Type 'y' to get another card, type 'n' to pass: ")
        #Player draws a card and update the player score
        if get_card == 'y':
            player_turn(player_list)
            player_score = sum(player_list)
            if player_score >21:
                #End the turn
                u_input = 'n'
                print(f"Your cards: {player_list}, final score: {player_score}\nComputer's cards: {dealer_list}, final score: {dealer_score}")
                print(compare_result(player_score, dealer_score))
                break
            print(f"Your cards: {player_list}, current score: {player_score}\nComputer's cards: {dealer_list}")
        #Player stops drawing a card, dealer's turn to draw cards if dealer's score < 17
        elif get_card == 'n':
            #End the game
            u_input='n'
            while dealer_score < 17:
                dealer_turn(dealer_list)
                dealer_score = sum(dealer_list)
            
            print(f"Your cards: {player_list}, final score: {player_score}\nComputer's cards: {dealer_list}, final score: {dealer_score}")
            print(compare_result(player_score, dealer_score))
