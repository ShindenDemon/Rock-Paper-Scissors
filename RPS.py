import random
from collections import Counter

def player(prev_play, opponent_history=[]):
    # Variable for the first move
    guess = "P"
    # Dictionary with counterplays
    counter_play = {"P": "S", "S": "R", "R": "P"}

    # Saving opponent moves
    if prev_play:
        opponent_history.append(prev_play)  
    else:
        return guess    # First move 

    # Handling Kris
    if len(opponent_history) == 1:        
        return guess    # Make the same move for the second round
    elif len(opponent_history) == 2:
        return counter_play[prev_play]  # Counterplay in the third round, necessary for handling Kris    
    else:     
        return prev_play    # Trap Kris in a losing loop

    # Handling Quincy
    # As Quincy do a fixed five length pattern, opponent_history must have at least five values for Quincy's pattern checking
    if len(opponent_history) >=6:
        last_five = opponent_history[-5:]   # Last five opponent moves
        count = Counter(last_five)  # Count values of R,P,S in the last five opponent moves in order to detect Quincy's pattern

    # As pattern is ["R","R","P","P",S] if count have R = 2, P = 2 and S = 1, it may be Quincy's play
        
        ''' Write code to detect the pattern, identify which part of the sequence is being executed, 
            and then apply countermeasures 
        '''
    
        
        
    
        
    
    

    

   
