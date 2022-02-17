from card import Card
import utils
import json


def prompt_card(flashcards):
    while True:
        flashcards.print_message('The card:\n')
        term = flashcards.user_input()
        if term in flashcards.card_dict:
            flashcards.print_message(f'The card "{term}" already exists. Try again:\n')
        else:
            break
    while True:
        flashcards.print_message('The definition of the card:\n')
        definition = flashcards.user_input()
        if definition in flashcards.card_dict.values():
            flashcards.print_message(f'The definition "{definition} already exists. Try again:\n')
        else:
            break
    flashcards.print_message(f'The pair ("{term}":"{definition}") has been added\n')
    return {'term': term, 'definition': definition}


def import_cards(file):
    try:
        with open(file, 'r') as handle:
            data = json.loads(handle.read())
        if 'cards' not in data:
            data = {'cards': data, 'stats': {}}
        return data
    except OSError:
        return False


def export_cards(file, flashcards):
    try:
        data = {'cards': {}, 'stats': {}}
        for card in flashcards.card_dict:
            data['cards'][card] = flashcards.card_dict[card]
        for stat in flashcards.stats:
            data['stats'][stat] = flashcards.stats[stat]
        with open(file, 'w') as handle:
            handle.write(json.dumps(data))
            return True
    except OSError:
        return False


def prompt_cards(cards, flashcards):
    for card in cards:
        flashcards.print_message('Print the definition of "{}"\n'.format(card['term']))
        user_def = flashcards.user_input()
        if card['definition'] == user_def:
            flashcards.print_message('Correct!\n')
        else:
            flashcards.print_message('Wrong. The right answer is "{}"'.format(card['definition']))
            flashcards.log_incorrect(card['term'])
            alt = False
            for c in flashcards.card_dict:
                if flashcards.card_dict[c] == user_def:
                    alt = c
                    break
            if alt:
                flashcards.print_message(', but your definition is correct for: "{}"\n'.format(alt))
            else:
                flashcards.print_message('.\n')


def main():
    flashcards = Card()
    end = False
    while not end:
        action = utils.menu(flashcards)
        if action == 'exit':
            end = True
        elif action == 'add':
            card = prompt_card(flashcards)
            flashcards.add_card(card['term'], card['definition'])
        elif action == 'remove':
            flashcards.print_message('Which card?\n')
            term = flashcards.user_input()
            if term not in flashcards.card_dict:
                flashcards.print_message(f'Can\'t remove "{term}": there is no such card\n')
                continue
            flashcards.delete_card(term)
            flashcards.print_message('The card has been removed.\n')
        elif action == 'import':
            flashcards.print_message('File name:\n')
            file_name = flashcards.user_input()
            contents = import_cards(file_name)
            if not contents:
                flashcards.print_message('File not found.\n')
                continue
            count = flashcards.load_cards(contents)
            flashcards.print_message(f'{count} cards have been loaded.\n')
        elif action == 'export':
            flashcards.print_message('File name:\n')
            file_name = flashcards.user_input()
            result = export_cards(file_name, flashcards)
            if not result:
                flashcards.print_message('Export failed\n')
            else:
                flashcards.print_message(f'{len(flashcards.card_dict)} cards have been saved.\n')
        elif action == 'ask':
            flashcards.print_message('How many times to ask?\n')
            number = int(flashcards.user_input())
            prompt_cards(flashcards.get_random_cards(number), flashcards)
        elif action == 'hardest card':
            cards = flashcards.get_hardest()
            if not cards:
                flashcards.print_message('There are no cards with errors\n')
            elif len(cards['term']) == 1:
                flashcards.print_message('The hardest card is "{}". You have {} errors answering it\n'.format(cards['term'][0], cards['errors']))
            else:
                terms = '", "'.join(cards['term'])
                flashcards.print_message(f'The hardest cards are "{terms}"\n')
        elif action == 'reset stats':
            flashcards.reset_stats()
            flashcards.print_message('Card statistics have been reset.\n')
        elif action == 'log':
            flashcards.print_message('File name:\n')
            output_to = flashcards.user_input()
            flashcards.save_log(output_to)
            flashcards.print_message('The log has been saved\n')
    flashcards.print_message('Bye bye!\n')


if __name__ == '__main__':
    main()
