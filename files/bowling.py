# Example string format: X|X|X|X|X|X|X|X|X|X||XX

def bowling(string):
    clean_string = string.replace('|', '')
    final_score = 0

    # Should read all numbers and compute the final result
    for i in range(10):
        if clean_string[i] == "X":
            final_score += compute_X(clean_string, i)
            
            
    return final_score

        
def compute_X(clean_string, i):
    score = 10
    next_string = clean_string[i+1]
    next_next_string = clean_string[i+2]
    
    if (next_string == "X"):
        score += 10
    if (next_next_string== "X"):
        score += 10
    else:
        score += int(next_next_string)
    
    return score
    