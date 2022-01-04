import random


class Card:
    def __init__(self):
        self.card_dict = {}

    def add_card(self, term, definition):
        self.card_dict[term] = definition

    def delete_card(self, term):
        del self.card_dict[term]

    def load_cards(self, cards):
        for card in cards:
            self.card_dict[card] = cards[card]
        return len(cards)

    def get_random_cards(self, number):
        cards = []
        for i in range(0, number):
            key = random.choice(list(self.card_dict.keys()))
            cards.append({'term': key, 'definition': self.card_dict[key]})
        return cards
