# Program : assignment2-carddraw.py
# This program deals (prints out) 5 cards
# Author: Hewa Orang

import requests

SHUFFLE_URL = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
DRAW_URL = "https://deckofcardsapi.com/api/deck/<<deck_id>>/draw/?count=5"

# Shuffle and create a new deck
response = requests.get(SHUFFLE_URL)
deck_data = response.json()
deck_id = deck_data['deck_id']

# Draw 5 cards from the deck
draw_url = DRAW_URL.replace("<<deck_id>>", deck_id)
response = requests.get(draw_url)
cards_data = response.json()

# Print the drawn cards
for card in cards_data['cards']:
    print(f"{card['value']} of {card['suit']}") 

# Check for special hands (e.g., pairs, three of a kind, etc.)
cards = cards_data['cards']
values = [card['value'] for card in cards]
suits = [card['suit'] for card in cards]
