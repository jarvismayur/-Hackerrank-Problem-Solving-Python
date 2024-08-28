# Python
| Concept              | Hackerrank Problem                                         | Difficulty | Time Complexity | Space Complexity | Score |
|----------------------|------------------------------------------------------------|------------|-----------------|------------------|-------|
| [List Comprehensions](#list-comprehensions)     | [List Comprehension](https://www.hackerrank.com/challenges/list-comprehensions/problem) | Easy       | O(n)            | O(n)             | 10    |


## Alphabet Rangoli
**Definition**: Alphabet Rangoli is a pattern design made with alphabetic characters arranged in a symmetrical, colorful pattern. It is often used in coding challenges to test skills related to loops, string manipulation, and formatting.
    
- **Syntax**:
```
Create a Rangoli of size n, where n represents the number of rows and columns in the pattern.
```

- **Example**:
```python
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
```

- **Output**:
```css
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
```

- **Common Problems**:
    - **Problem**: Understanding the pattern structure can be challenging.
        - **Solution**: Break down the pattern into smaller components and build each component step-by-step.
    
    - **Problem**: Handling large values for n may lead to formatting issues or excessive output.
        - **Solution**: Ensure the pattern width is calculated correctly and consider using efficient string operations.

## Arithmetic Operators
## Capitalize!
## Check Strict Superset
## Check Subset
## Designer Door Mat
## Find a string
## Find the Runner-Up Score!
## Finding the percentage
## Introduction to Sets
## itertools.combinations()
## itertools.combinations_with_replacement()
## itertools.permutations()
## itertools.product()
## List Comprehensions
**Definition**: List comprehension is a concise way to create lists in Python. It is a syntactic construct that allows you to create a new list by applying an expression to each item in an existing iterable.

- **Syntax**:
    ```python
    [expression for item in iterable if condition]
    ```

- **Examples**:
    ```python
    # Example 1: Creating a list of squares
    squares = [x**2 for x in range(10)]
    print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

    # Example 2: Filtering even numbers
    evens = [x for x in range(10) if x % 2 == 0]
    print(evens)  # Output: [0, 2, 4, 6, 8]
    ```

- **Common Problems**:
    - **Problem**: List comprehension can be confusing when it involves complex logic.
      - **Solution**: Break down the logic into smaller parts or use traditional loops for better readability.
    
    - **Problem**: Memory issues with large iterables.
      - **Solution**: Consider using generator expressions if the list is too large to fit into memory.
## Lists
## Loops
## Merge The Tools
My Frist code with only one test case passed 
```
    def merge_the_tools(string, k):
        new_str = []
        # your code goes here
        str_list = string.split()
        new_str_list = []
        for a in str_list:
            for b in a:
                new_str_list.append(b)
        count_str_list = len(new_str_list)
        parts = int(count_str_list/k)
        str_arr= []
        for i in range(1,len(new_str_list)+1):
            new_str.append(new_str_list[i-1])
            if i != 0:
                if i % parts == 0:
                    str_arr.append("".join(new_str))
                    new_str = []
            
        for s in str_arr:
            new_string = ""
            for char in s:
                if char not in new_string:
                    new_string += char
```
My Last optimized code the all the test case pass
```
    def merge_the_tools(string, k):
        for a in range(0, len(string), k):
            substring = string[a:a+k]
            seen = ""
            for b in substring:
                if b not in seen:
                    seen= seen+ b
            print(seen)
    
    
        

    if __name__ == '__main__':
        string, k = input(), int(input())
        merge_the_tools(string, k)
```
## Mutations
## Nested Lists
## No Idea!
## Print Function
## Python Division
## Python If-Else
## Say Hello World With Python
## Set .add().
## Set .difference() Operation
## Set .discard(), .remove() & .pop()
## Set .intersection() Operation
## Set .symmetric_difference() Operation
## Set .union() Operation
## Set Mutations
## String Formatting
## String Split and Join
## String Validators
## sWAP cASE
## Symmetric Difference
## Text Alignment
## Text Wrap
## The Captain's Room
## The Minion Game
## Tuples
## What's Your Name
## Write a function
