class Card:
    def __init__(self):
        self.card_dict = {}

    def add_card(self, term, definition):
        self.card_dict[term] = definition

    def delete_card(self, term):
        del self.card_dict[term]

    def load_file(self, file_name):
        pass

    def save_to_file(self, file_name):
        pass

    def get_random_cards(self):
        pass


def prompt_card(cards, i):



def main():
    print('Input the number of cards:')
    number = int(input())
    terms = {}
    definitions = {}
    for i in range(number):
        repeat = 1
        print('The term for card #{}'.format(i + 1))
        while True:
            term = input()
            if term in terms:
                print('The term "{}" already exists. Try again:'.format(term))
            else:
                break
        print('The definition for card #{}'.format(i + 1))
        while True:
            definition = input()
            if definition in definitions:
                print('The definition "{}" already exists. Try again:'.format(definition))
            else:
                break
        terms[term] = definition
        definitions[definition] = term
    for term in terms:
        print('Print the definition of "{}"'.format(term))
        user_def = input()
        if (terms[term] == user_def):
            print('Correct!')
        else:
            print('Wrong. The right answer is "{}"'.format(terms[term]), end='')
            if user_def in definitions:
                print(', but your definition is correct for: "{}"'.format(definitions[user_def]))
            else:
                print('.')


if __name__ == '__main__':
    main()
