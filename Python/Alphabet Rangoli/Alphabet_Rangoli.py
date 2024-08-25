def print_rangoli(size):
    # your code goes here
    # Define the alphabet
    import string
    alphabet = string.ascii_lowercase
    
    # Determine the width of the final rangoli (width of the largest line)
    width = 4 * size - 3
    
    # Generate the top half of the rangoli (including the middle line)
    lines = []
    for i in range(size):
        # Generate the sequence: e.g., for size 5: 'e-d-c-b-a'
        left_part = '-'.join(alphabet[size-1:i:-1])
        middle_part = alphabet[i]
        right_part = left_part[::-1]
        full_line = left_part + '-' + middle_part + '-' + right_part if left_part else middle_part
        lines.append(full_line.center(width, '-'))
    
    # Complete the rangoli by mirroring the top half (excluding the middle line)
    full_rangoli = '\n'.join(lines[::-1] + lines[1:])
    
    print(full_rangoli)

# Sample Input

