from card import Card
import utils
import json


def prompt_card(cards):
    while True:
        print('The card:')
        term = input()
        if term in cards:
            print(f'The card "{term}" already exists. Try again:')
        else:
            break
    while True:
        print('The definition of the card:')
        definition = input()
        if definition in cards.values():
            print(f'The definition "{definition} already exists. Try again:')
        else:
            break
    print(f'The pair ("{term}":"{definition}") has been added')
    return {'term': term, 'definition': definition}


def import_cards(file):
    try:
        with open(file, 'r') as handle:
            cards = json.loads(handle.read())
        return cards
    except OSError:
        return False


def export_cards(file, cards):
    try:
        with open(file, 'w') as handle:
            handle.write(json.dumps(cards))
            return True
    except OSError:
        return False


def prompt_cards(cards, all_cards):
    for card in cards:
        print('Print the definition of "{}"'.format(card['term']))
        user_def = input()
        if card['definition'] == user_def:
            print('Correct!')
        else:
            print('Wrong. The right answer is "{}"'.format(card['definition']), end='')
            alt = False
            for c in all_cards:
                if all_cards[c] == user_def:
                    alt = c
                    break
            if alt:
                print(', but your definition is correct for: "{}"'.format(alt))
            else:
                print('.')


def main():
    flashcards = Card()
    end = False
    while not end:
        action = utils.menu()
        if action == 'exit':
            end = True
        elif action == 'add':
            card = prompt_card(flashcards.card_dict)
            flashcards.add_card(card['term'], card['definition'])
        elif action == 'remove':
            print('Which card?')
            term = input()
            if term not in flashcards.card_dict:
                print(f'Can\'t remove "{term}": there is no such card')
                continue
            flashcards.delete_card(term)
            print('The card has been removed.')
        elif action == 'import':
            print('File name:')
            file_name = input()
            contents = import_cards(file_name)
            if not contents:
                print('File not found.')
                continue
            count = flashcards.load_cards(contents)
            print(f'{count} cards have been loaded.')
        elif action == 'export':
            print('File name:')
            file_name = input()
            result = export_cards(file_name, flashcards.card_dict)
            if not result:
                print('Export failed')
            else:
                print(f'{len(flashcards.card_dict)} cards have been saved.')
        elif action == 'ask':
            print('How many times to ask?')
            number = int(input())
            prompt_cards(flashcards.get_random_cards(number), flashcards.card_dict)
    print('Bye bye!')
    '''
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
    '''


if __name__ == '__main__':
    main()
