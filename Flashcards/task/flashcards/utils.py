def menu(flashcards):
    while True:
        flashcards.print_message('Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats)\n')
        action = flashcards.user_input()
        if action not in ['add', 'remove', 'import', 'export', 'ask', 'exit', 'log', 'hardest card',
                          'reset stats']:
            flashcards.print_message('Wrong action\n')
        else:
            return action
