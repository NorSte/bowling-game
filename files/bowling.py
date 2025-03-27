# Example string format: X|X|X|X|X|X|X|X|X|X||XX

def bowling(string):
    clean_string = string.replace('|', '')
    final_score = 0

    # Should read all numbers and compute the final result
    for i in range(len(clean_string) - 2):
        if (clean_string[i] == "X"):
            final_score += compute_X(clean_string, i)
        elif (clean_string[i] == "/"):
            final_score += compute_spare(clean_string, i)
        elif (clean_string[i]  == "-"):
            final_score += 0
            
    return final_score

# Computes and returns the value of X with the respective "nexts"
def compute_X(clean_string, i):
    score = 10
    next_string = clean_string[i+1]
    next_next_string = clean_string[i+2]
    
    if (next_string == "X"):
        score += 10
    elif (next_string == "-"):
        score += 0
    else:
        score += int(next_string)
        
    if (next_next_string== "X"):
        score += 10
    elif (next_next_string == "/"):
        if(next_string == "-"):
            score += 10 
        else:    
            score += 10 - int(next_string)
    elif (next_next_string == "-"):
        score += 0
    else:
        score += int(next_next_string)
    
    return score

def compute_spare(clean_string, i):
    score = 10
    next_string = clean_string[i+1]
    
    if (next_string == "X"):
        score += 10
    elif (next_next_string == "-"):
        score += 0
    else:
        score += int(next_string)
    
    return score
    
    