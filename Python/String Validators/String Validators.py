if __name__ == '__main__':
    s = input()
    print(any(c.isalnum() for c in s))   # Check if there's any alphanumeric character
    print(any(c.isalpha() for c in s))   # Check if there's any alphabetical character
    print(any(c.isdigit() for c in s))   # Check if there's any digit
    print(any(c.islower() for c in s))   # Check if there's any lowercase character
    print(any(c.isupper() for c in s))   # Check if there's any uppercase character
