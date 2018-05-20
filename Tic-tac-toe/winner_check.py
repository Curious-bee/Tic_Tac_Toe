def winner_check(number,player1,player2):
    
    if (number[0]==number[1]==number[2]==player1 or number[3]==number[4]==number[5]==player1 or number[6]==number[7]==number[8]==player1 or number[0]==number[3]==number[6]==player1 or number[1]==number[4]==number[7]==player1 or number[8]==number[5]==number[2]==player1 or number[6]==number[4]==number[2]==player1 or number[0]==number[4]==number[8]==player1):
        
        return print("Player 1 Won!!")
    
    elif (number[0]==number[1]==number[2]==player2 or number[3]==number[4]==number[5]==player2 or number[6]==number[7]==number[8]==player2 or number[0]==number[3]==number[6]==player2 or number[1]==number[4]==number[7]==player2 or number[8]==number[5]==number[2]==player2 or number[6]==number[4]==number[2]==player2 or number[0]==number[4]==number[8]==player2):
            
        return print("Player 2 Won!!") 
    else:
        return False