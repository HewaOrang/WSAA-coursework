# Program : assignment2-carddraw.py
# This program deals (prints out) 5 cards and checks for special hands (flush, four of a kind, three of a kind, pair)
# Author: Hewa Orang

import requests

SHUFFLE_URL = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
DRAW_URL = "https://deckofcardsapi.com/api/deck/{}/draw/?count=5"

# Shuffle and create a new deck
response = requests.get(SHUFFLE_URL)
deck_data = response.json()
deck_id = deck_data['deck_id']

# Draw 5 cards from the deck
draw_response = requests.get(DRAW_URL.format(deck_id))
cards_data = draw_response.json()

# Print the drawn cards
print("Your cards:")
for card in cards_data['cards']:
    print(f"{card['value']} of {card['suit']}") 

# Check for special hands
cards = cards_data['cards']
values = [card['value'] for card in cards]
suits = [card['suit'] for card in cards]

# Count occurrences of each value
value_counts = {}
for value in values:
    value_counts[value] = value_counts.get(value, 0) + 1

# Check for all same suit
if len(set(suits)) == 1:
    print(" Congratulations! You got a FLUSH (all same suit)!")

# Check for four of a kind
elif 4 in value_counts.values():
    print(" Congratulations! You got FOUR OF A KIND!")
# Check for three of a kind
elif 3 in value_counts.values():
    print(" Congratulations! You got THREE OF A KIND!")
# Check for pair
elif 2 in value_counts.values():
    print(" Congratulations! You got a PAIR!")
else:
    print("No special hand this time. Better luck next time!")