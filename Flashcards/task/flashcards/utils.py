def menu():
    while True:
        print('Input the action (add, remove, import, export, ask, exit)')
        action = input()
        if action not in ['add', 'remove', 'import', 'export', 'ask', 'exit']:
            print('Wrong action')
        else:
            return action
