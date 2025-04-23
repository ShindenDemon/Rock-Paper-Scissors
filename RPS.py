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
        Quincy_patterns = {1:['R','R','P','P','S'],
                           2:['R','P','P','S','R'],        
                           3:['P','P','S','R','R'],     # Possible Quincy´s patterns     
                           4:['P','S','R','R','P'], 
                           5:['S','R','R','P','P']}

        for pattern in Quincy_patterns.values():    
            if last_five == pattern:    # Check if Quincy´s pattern is being executed    
                is_Quincy == True       # Identifying Quincy as opponent 
        
        ''' Identify which part of the sequence is being executed, 
            and then apply countermeasures. Maybe using some variables (is_xxxx)
            would help bot handling easily.
        '''
    
        
        
    
        
    
    

    

   
