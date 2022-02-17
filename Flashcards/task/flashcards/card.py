import random
from io import StringIO


class Card:
    def __init__(self):
        self.card_dict = {}
        self.stats = {}
        self.log = StringIO()

    def add_card(self, term, definition):
        self.card_dict[term] = definition

    def delete_card(self, term):
        del self.card_dict[term]

    def load_cards(self, data):
        for card in data['cards']:
            self.card_dict[card] = data['cards'][card]
        for stat in data['stats']:
            self.stats[stat] = data['stats'][stat]
        return len(data['cards'])

    def get_random_cards(self, number):
        cards = []
        for i in range(0, number):
            key = random.choice(list(self.card_dict.keys()))
            cards.append({'term': key, 'definition': self.card_dict[key]})
        return cards

    def log_incorrect(self, term):
        if term not in self.stats:
            self.stats[term] = 1
        else:
            self.stats[term] += 1

    def get_hardest(self):
        temp_stats = {}
        temp_numbers = []
        for term in self.stats:
            if self.stats[term] not in temp_stats:
                temp_stats[self.stats[term]] = [term]
            else:
                temp_stats[self.stats[term]].append(term)
            temp_numbers.append(self.stats[term])
        if len(temp_numbers) == 0:
            return False
        m = max(temp_numbers)
        return {'term': temp_stats[m], 'errors': m}

    def reset_stats(self):
        self.stats = {}

    def print_message(self, message):
        self.log.write(message)
        print(message, end='')

    def user_input(self):
        value = input()
        self.log.write(f'{value}\n')
        return value

    def save_log(self, file_name):
        with open(file_name, 'w') as output:
            output.write(self.log.getvalue())
        self.print_message('The log has been saved')
