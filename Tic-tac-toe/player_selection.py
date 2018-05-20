def player_selection():
    selection=''
    while not (selection== 'X' or selection =='O'):
        selection=input("Player 1 choose your symbol 'X' or 'O': ").upper()
    if selection=='X':
        print("\nPlayer 1 is 'X' & Player 2 is 'O'")
    else:
        print("\nPlayer 1 is 'O' & Player 2 is 'X'")
    return selection