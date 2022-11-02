"""
Given a string, find the length of the longest substring
in it with no more than K distinct characters

Input: String="araaci", K=2
Ouput: 4, "araa"

def long_length(st, k):

    set = {} to remember how many character your have
    start_window = 0 
    length = 0

    iterate the str
    "araaci"
start|
end      |
    
    add a : 3 
    add r : 1

    while len(len(set) > k)
        char in index start
        move start window

        check if st[index] is 0:
            del it

    check if set len(str) is bigger than k if so move start window until is not
"""


def longest_substring(st, k):
    char_set = {}
    start_window = 0 
    length = 0
    max_length = 0

    for end_window in range(len(st)):
        charc = st[end_window]

        if charc not in char_set:
            char_set[charc] = 0
        
        char_set[charc] += 1
        length += 1

        while len(char_set) > k:
            left_char = st[start_window]
            start_window += 1
            length -= 1

            char_set[left_char] -= 1

            if char_set[left_char] == 0:
                del char_set[left_char]
            
        max_length = max(max_length, length)
    
    return max_length

print(longest_substring("araaci", 2))
