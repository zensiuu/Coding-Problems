def first_non_repeating_char(s):
    # in pyhton, the 'dictionary' type is a built-in hash map 
    counts={}
    # step1 : Build the frequency map(o(n)time)
    for char in s :
        counts[char]=counts.get(char,0)+1
    
    # step2: find the first char with frequency 1 (o(n) time )
    for char in s : 
        if counts[char] == 1 :
            return char
    return None 
# Example usage :
print(first_non_repeating_char("swiss")) # output: 'w'
