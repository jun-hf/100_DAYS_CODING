
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
