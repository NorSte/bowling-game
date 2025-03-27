# Example string format: X|X|X|X|X|X|X|X|X|X||XX

def bowling(string):
    clean_string = string.replace('|', '')
    score = 0

    # Should read all numbers and compute the final result
    for i in range(10):
        if clean_string[i] == "X":
            score += compute_X(clean_string, i)
        
def compute_X(clean_string, i):
    score = 10
    
    if (clean_string[i+1] == "X"):
        score += 10
    if (clean_string[i+2] == "X"):
        score += 10
    
    return score
    