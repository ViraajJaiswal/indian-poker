#Create the game Te'en Patti in Python

import random

def rank_hand(hand):
    hand.sort(reverse=True)
    
    if all(hand[i][0] == hand[i + 1][0] + 1 and hand[i][1] == hand[i + 1][1] for i in range(len(hand) - 1)):
        return "Straight Flush", hand[0][0]
    
    for value, _ in hand:
        if hand.count((value, _)) == 4:
            return "Four of a Kind", value
    
    if len(set(hand)) == 2 and (hand.count(hand[0]) == 3 or hand.count(hand[0]) == 2):
        return "Full House", hand[0][0]
    
    if len(set([card[1] for card in hand])) == 1:
        return "Flush", hand[0][0]
    
    if all(hand[i][0] == hand[i + 1][0] + 1 for i in range(len(hand) - 1)
            ) or [card[0] for card in hand] == [14, 5, 4]:
        return "Straight", hand[0][0]
    
    for value, _ in hand:
        if hand.count((value, _)) == 3:
            return "Three of a Kind", value
    
    pairs = [value for value in set([card[0] for card in hand]) if [card[0] for card in hand].count(value) == 2]
    if len(pairs) == 2:
        return "Two Pairs", max(pairs)
    
    for value, _ in set(hand):
        if hand.count((value, _)) == 2:
            return "Pair", value
    
    return "High Card", hand[0][0]

def create_deck():
    ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    deck = [(rank, suit) for rank in ranks for suit in suits]
    random.shuffle(deck)
    return deck

def deal_cards():
    deck = create_deck()
    player1_hand = [deck.pop() for _ in range(3)]
    player2_hand = [deck.pop() for _ in range(3)]
    return player1_hand, player2_hand

def display_hand(hand):
    return [f"{rank} of {suit}" for rank, suit in hand]

def determine_winner(player1_hand, player2_hand):
    rank1, value1 = rank_hand(player1_hand)
    rank2, value2 = rank_hand(player2_hand)

    if value1 > value2:
        return "Player 1 wins!"
    elif value1 < value2:
        return "Player 2 wins!"
    else:
        return "It's a tie!"

def play_game():
    print("Welcome to Teen Patti!")
    player1_hand, player2_hand = deal_cards()

    print(f"Player 1 hand: {display_hand(player1_hand)}")
    print(f"Player 2 hand: {display_hand(player2_hand)}")

    result = determine_winner(player1_hand, player2_hand)
    print(result)

if __name__ == "__main__":
    play_game()
