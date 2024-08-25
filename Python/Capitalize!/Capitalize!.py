

# Complete the solve function below.
def solve(s):
    # Regular expression to find words while preserving spaces
    def capitalize_match(match):
        word = match.group()
        if word.isalpha():
            return word[0].upper() + word[1:].lower()
        return word

    # Use regular expression to find all words and capitalize them
    capitalized_string = re.sub(r'\b\w+\b', capitalize_match, s)
    
    print(capitalized_string)
    return capitalized_string


