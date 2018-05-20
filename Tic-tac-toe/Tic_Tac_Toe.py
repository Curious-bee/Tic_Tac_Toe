import Board
import winner_check
import player_selection

# Welcome Message

print("####  Welcome  ####\n#####    To   ##### \n#### Tie-Tac-Toe ####\n")
welcome=input("Do you want to play? (y/n): ").upper()
if welcome=='Y':
	game_on=True
else:
	game_on=False

# Game logic is under this while loop if game_on is Flase, Game will end.

while(game_on==True):
	numbers=[x for x in range(1,10)]
	Board.new_board(numbers)

# Player's Markers are received and assigned 

	player1=player_selection.player_selection()
	player2=''
	selected_opts=[]
	tot_turn=1
	if player1=='X':
	    player2='O'
	else:
	    player2='X'


# New board with numbers is printed
	Board.new_board(numbers)  

# Game loop for player inputs. check for winner, and if the board is full (i.e 10 turns) it's a TIE 
	while tot_turn<=10:     
	    if tot_turn==10:    # It's a Tie
	         print("It's a Tie well played both of you :)")
	         break
	    elif tot_turn%2==0: #player 2's turn
	        option=int(input('\nPlayer 2 choose your position on the board [1-9]: '))
	        while option in selected_opts:
	            option=int(input('\nWrong Choice\n Choose an option which is not already taken\nPlayer 2 choose your position on the board [1-9]: '))
	        selected_opts.append(option)
	        numbers[option-1]=player2
	        Board.new_board(numbers)
	        if winner_check.winner_check(numbers,player1,player2)==False:
	        	pass
	        else:
	        	winner_check.winner_check(numbers,player1,player2) #Player 2 won
	        	break
	    else:               #player 1's turn
	        option=int(input('\nPlayer 1 choose your position on the board [1-9]: '))
	        while option in selected_opts:
	            option=int(input('\nWrong Choice\n Choose an option which is not already taken\nPlayer 1 choose your position on the board [1-9]: '))
	        selected_opts.append(option)
	        numbers[option-1]=player1
	        Board.new_board(numbers)
	        if winner_check.winner_check(numbers,player1,player2)==False:
	        	pass
	        else:
	        	winner_check.winner_check(numbers,player1,player2) #Player 2 won
	        	break
	    tot_turn+=1

	replay=input('Do you wanna  play again (Y/N): ').upper()
	if replay=='Y':
		game_on==True    # New game
	else:
		game_on==False   #End game