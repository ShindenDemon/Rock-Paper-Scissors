import random

def player(prev_play, opponent_history=[]):
    # Variable for the first move
    guess = "P"
    counter_play = {"P": "S", "S": "R", "R": "P"}

    # Saving opponent moves
    if prev_play:
        opponent_history.append(prev_play)  
    else:
        counter = 0 # Variable to time the counter
        return guess  # First move 

    # Handle Kris
    if len(opponent_history) == 1:        
        return guess
    elif len(opponent_history) == 2:
        return counter_play[prev_play]    
    else:     
        print(len(opponent_history))           
        return prev_play
        
        
    
        
    
    

    

   
