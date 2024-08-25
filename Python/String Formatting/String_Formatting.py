def print_formatted(number):
# Determine the width needed for binary representation of the highest number
    width = len(bin(number)[2:])

    # Loop through each number from 1 to number (inclusive)
    for i in range(1, number + 1):
        # Convert and format the values
        decimal_value = str(i).rjust(width)
        octal_value = oct(i)[2:].rjust(width)
        hexadecimal_value = hex(i)[2:].upper().rjust(width)
        binary_value = bin(i)[2:].rjust(width)
        
        # Print all values in the specified format
        print(f"{decimal_value} {octal_value} {hexadecimal_value} {binary_value}")

