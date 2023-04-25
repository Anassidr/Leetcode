import re 

results = "424253-1323244-11-1"

def find_longest(results):

    guesses = re.findall(r'-?\d', results)

    longest_series = 0
    current_series = 0 

    for guess in guesses:
        if guess == "-1": 
            current_series = 0
        elif not guess.isdigit() or int(guess) < 1 or int(guess) > 6:
            return "INVALID"
        else:
            current_series += 1 
            longest_series = max(longest_series, current_series)
    return longest_series

print(find_longest(results))

# can improve space complexity 