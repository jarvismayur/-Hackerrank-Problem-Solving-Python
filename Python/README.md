# Python

- [Python](#python)
  - [Alphabet Rangoli-](#alphabet-rangoli-)
  - [Arithmetic Operators](#arithmetic-operators)
  - [Capitalize!](#capitalize)
  - [Check Strict Superset](#check-strict-superset)
  - [Check Subset](#check-subset)
  - [Designer Door Mat](#designer-door-mat)
  - [Find a string](#find-a-string)
  - [Find Angle MBC](#find-angle-mbc)
  - [Find the Runner-Up Score!](#find-the-runner-up-score)
  - [Finding the percentage](#finding-the-percentage)
  - [Integers Come In All Sizes](#integers-come-in-all-sizes)
  - [Introduction to Sets](#introduction-to-sets)
  - [itertools.combinations()](#itertoolscombinations)
  - [itertools.combinations\_with\_replacement()](#itertoolscombinations_with_replacement)
  - [itertools.permutations()](#itertoolspermutations)
  - [itertools.product()](#itertoolsproduct)
  - [List Comprehensions](#list-comprehensions)
  - [Lists](#lists)
  - [Loops](#loops)
  - [Merge The Tools](#merge-the-tools)
  - [Mod Divmod](#mod-divmod)
  - [Mutations](#mutations)
  - [Nested Lists](#nested-lists)
  - [No Idea!](#no-idea)
  - [Polar Coordinates](#polar-coordinates)
  - [Power - Mod Power](#power---mod-power)
  - [Print Function](#print-function)
  - [Python Division](#python-division)
  - [Python If-Else](#python-if-else)
  - [Say Hello World With Python](#say-hello-world-with-python)
  - [Set .add().](#set-add)
  - [Set .difference() Operation](#set-difference-operation)
  - [Set .discard(), .remove() \& .pop()](#set-discard-remove--pop)
  - [Set .intersection() Operation](#set-intersection-operation)
  - [Set .symmetric\_difference() Operation](#set-symmetric_difference-operation)
  - [Set .union() Operation](#set-union-operation)
  - [Set Mutations](#set-mutations)
  - [String Formatting](#string-formatting)
  - [String Split and Join](#string-split-and-join)
  - [String Validators](#string-validators)
  - [sWAP cASE](#swap-case)
  - [Symmetric Difference](#symmetric-difference)
  - [Text Alignment](#text-alignment)
  - [Text Wrap](#text-wrap)
  - [The Captain's Room](#the-captains-room)
  - [The Minion Game](#the-minion-game)
  - [Triangle Quest](#triangle-quest)
  - [Triangle Quest 2](#triangle-quest-2)
  - [Tuples](#tuples)
  - [What's Your Name](#whats-your-name)
  - [Write a function](#write-a-function)

## Alphabet Rangoli- 

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

- **Common Problems**:
    - **Problem**: Understanding the pattern structure can be challenging.
        - **Solution**: Break down the pattern into smaller components and build each component step-by-step.
    
    - **Problem**: Handling large values for n may lead to formatting issues or excessive output.
        - **Solution**: Ensure the pattern width is calculated correctly and consider using efficient string operations.

## Arithmetic Operators
**Definition**: Arithmetic operators are symbols used to perform mathematical operations on numeric values. These operators are fundamental to many programming tasks and are supported by most programming languages.

- **Operators and Their Symbols**:

| Operator	|Symbol	|Description	|Example|
|-----------|-------|---------------|-------|
|Addition	|+|	Adds two operands   |a + b|
|Subtraction	|-|	Subtracts the second operand from the first	|a - b|
|Multiplication	|*|	Multiplies two operands	|a * b|
|Division	|/|	Divides the numerator by the denominator	|a / b|
|Floor Division	|//|	Divides and returns the integer part	|a // b|
|Modulus	|%|	Returns the remainder of the division	|a % b|
|Exponentiation	|**|	Raises the first operand to the power of the second	|a ** b|
- **Examples**:

```python

# Addition
a = 10
b = 5
print(a + b)  # Output: 15

# Subtraction
print(a - b)  # Output: 5

# Multiplication
print(a * b)  # Output: 50

# Division
print(a / b)  # Output: 2.0

# Floor Division
print(a // b) # Output: 2

# Modulus
print(a % b)  # Output: 0

# Exponentiation
print(a ** b) # Output: 100000
```
- **Common Problems**:

    - **Problem**: Integer division might not work as expected if floating-point numbers are involved.
        - **Solution**: Ensure to use appropriate operators for integer or floating-point division based on the requirement.
    
    - **Problem**: The modulo operator can produce different results with negative numbers depending on the language or environment.
        - **Solution**: Check the language-specific behavior of the modulo operator and test with various inputs.
## Capitalize!
**Definition**: The capitalize() method is a string method in Python that returns a copy of the string with its first character converted to uppercase and the rest of the characters converted to lowercase.

- **Syntax**:

```python
string.capitalize()
```
- **Examples**:

```python
# Example 1: Basic usage
text = "hello world"
print(text.capitalize())  # Output: "Hello world"

# Example 2: String with mixed case
text = "PYTHON is Fun"
print(text.capitalize())  # Output: "Python is fun"

# Example 3: String already capitalized
text = "Python"
print(text.capitalize())  # Output: "Python"
```
- **Common Problems**:

    - **Problem**: The method affects only the first character of the string and converts the rest to lowercase.

        - **Solution**: If you need to capitalize every word in the string, consider using the title() method instead.
    - **Problem**: The method does not handle non-alphabetic characters as expected.

        - **Solution**: Ensure that the string starts with an alphabetic character if you want to see the capitalization effect.
## Check Strict Superset
**Definition**: A set A is considered a strict superset of set B if A contains all elements of B and has at least one element not present in B. In other words, every element of B is in A, but A contains additional elements.

- **Syntax**:

```python
set_A > set_B
```
- **Examples**:

```python
# Example 1: Basic usage
set_A = {1, 2, 3, 4}
set_B = {2, 3}
print(set_A > set_B)  # Output: True

# Example 2: set_A is not a strict superset of set_B
set_A = {1, 2, 3}
set_B = {2, 3}
print(set_A > set_B)  # Output: False

# Example 3: Empty set as a subset
set_A = {1, 2, 3}
set_B = set()
print(set_A > set_B)  # Output: True
```
- **Common Problems**:

    - **Problem**: The comparison operator > checks if set_A is a strict superset of set_B, but it doesn’t account for subsets or equal sets.

        - **Solution**: Ensure that set_A has elements not present in set_B and that all elements of set_B are included in set_A.
    - **Problem**: Confusing the strict superset operator > with the superset operator >=.

        - **Solution**: Use > for strict superset checks and >= for checking if one set is a superset or equal to another set.
## Check Subset
**Definition**: A set A is considered a subset of set B if all elements of A are also elements of B. In other words, A is contained within B.

- **Syntax**:

```python
set_A <= set_B
```
- **Examples**:

```python
# Example 1: Basic usage
set_A = {1, 2}
set_B = {1, 2, 3, 4}
print(set_A <= set_B)  # Output: True

# Example 2: set_A is not a subset of set_B
set_A = {1, 5}
set_B = {1, 2, 3, 4}
print(set_A <= set_B)  # Output: False

# Example 3: Empty set is a subset of any set
set_A = set()
set_B = {1, 2, 3}
print(set_A <= set_B)  # Output: True
```
- **Common Problems**:

    - **Problem**: The subset operator <= checks if set_A is a subset of set_B, but it doesn’t account for whether set_A is equal to set_B.

        - **Solution**: Use set_A < set_B if you need to check if set_A is a proper subset (i.e., a subset that is not equal to set_B).
    - **Problem**: Confusing the subset operator <= with the proper subset operator <.

        - **Solution**: Use <= for subset checks and < for proper subset checks.
## Designer Door Mat

**Definition**: A Designer Door Mat is a pattern of text arranged in a specific design that often resembles a mat. The pattern usually consists of a central line of text surrounded by repeating elements to create a decorative effect.

- **Pattern Details**:

The mat consists of n lines, where n is an odd number.
The central line contains a specific pattern or text repeated, and the lines above and below gradually taper off to form a symmetrical design.
- **Example**:

```python
def print_door_mat(n, m):
    pattern = '.|.'
    
    # Top half including the middle line
    for i in range(1, n, 2):
        print((pattern * i).center(m, '-'))
    
    # Middle line
    print('WELCOME'.center(m, '-'))
    
    # Bottom half
    for i in range(n-2, 0, -2):
        print((pattern * i).center(m, '-'))

``` 
- Example:
```python
print_door_mat(7, 21)
```
- **Output**:

```diff
-----.|.-----
----.|.|.----
---.|.|.|.---
----WELCOME----
---.|.|.|.---
----.|.|.----
-----.|.-----
```
- **Common Problems**:

    - **Problem**: Misalignment of the pattern due to incorrect width (m) or n not being an odd number.

        - **Solution**: Ensure n is an odd number and m is sufficiently large to accommodate the pattern.
    - **Problem**: Understanding the pattern logic can be challenging.

        - **Solution**: Break down the pattern into smaller parts and understand how each part contributes to the final design.
## Find a string
**Definition**: Finding a substring involves checking whether a given substring exists within a larger string and determining its position if it does.

- **Methods**:

    - **Using find() Method**:

        - **Description**: The find() method returns the lowest index of the substring if it is found in the string. If the substring is not found, it returns -1.
        - **Syntax**:
        ```python
        string.find(substring)
        ```
        - **Examples**:
        ```python
        text = "Hello, world!"
        print(text.find("world"))  # Output: 7
        print(text.find("Python")) # Output: -1
        ```
    - **Using index() Method**:

        - **Description**: The index() method returns the lowest index of the substring if it is found in the string. If the substring is not found, it raises a ValueError.
        - **Syntax**:
        ```python
        string.index(substring)
        ```
        - **Examples**:
        ```python
        text = "Hello, world!"
        print(text.index("world"))  # Output: 7
        try:
            print(text.index("Python")) # Raises ValueError
        except ValueError:
            print("Substring not found")
        ```
    - **Using in Operator**:

        - **Description**: The in operator checks if a substring exists within a string and returns a boolean value.
        - **Syntax**:
        ```python
        substring in string
        ```
        - **Examples**:
        ```python
        text = "Hello, world!"
        print("world" in text)  # Output: True
        print("Python" in text) # Output: False
        ```
- **Common Problems**:

    - **Problem**: Using find() may be preferable for handling cases where the substring might not be present, as it returns -1 instead of raising an error.

        - **Solution**: Choose find() if you want a safe way to check for the presence of a substring without handling exceptions.
    - **Problem**: The index() method will raise an exception if the substring is not found, which can interrupt the program flow.

        - **Solution**: Use try-except blocks to handle potential exceptions when using index().

## Find Angle MBC 
**Definition**: The "Find Angle MBC" problem requires calculating the angle 
$\angle$ 𝑀𝐵𝐶  in a right-angled triangle using trigonometry. This problem helps practice basic trigonometric functions and understanding angles in geometric shapes.

- **Problem Statement**
You are given a right-angled triangle ABC, where M is the midpoint of the hypotenuse AB. You need to find the angle $\angle$ MBC (in degrees) using the lengths of sides AB and BC.

  - Input:
```
  The first line contains the length of side AB.
  The second line contains the length of side BC.
  ```
  - Output:
```
  Print the angle $\angle$ MBC in degrees.
  ```
    - Note:

        - Use the math.atan2 function to calculate the angle in radians.
        - Convert the angle to degrees using the math.degrees function.
- **Example**
    - Input:

```python

10
10
```
  - Output:

```python
45°
```

  - Explanation:

    - Since both sides AB and BC are equal, the triangle ABC is an isosceles right-angled triangle.
    - The angle $\angle$ MBC will be 45°.
- **Solution**
    - Algorithm:

        - Understanding the Triangle:

            - In the right-angled triangle ABC, side BC is adjacent to angle $\angle$ MBC.
            - Side AB is the hypotenuse.
            - The angle $\angle$ MBC can be found using trigonometric functions, specifically the arctangent (atan2) function.
        - Calculate the Angle:

            - Use the atan2(AB, BC) function to get the angle in radians.
            - Convert this angle from radians to degrees using the degrees function.
        - Format the Output:

            - Print the angle $\angle$ MBC rounded to the nearest integer followed by the degree symbol (°).
    - Python Code:
```python

import math

def find_angle_mbc(ab, bc):
    # Calculate the angle in radians
    angle_mbc_rad = math.atan2(ab, bc)
    # Convert the angle to degrees
    angle_mbc_deg = math.degrees(angle_mbc_rad)
    # Print the angle rounded to the nearest integer with the degree symbol
    print(f"{round(angle_mbc_deg)}°")

# Example usage
ab = int(input())  # Length of side AB
bc = int(input())  # Length of side BC
find_angle_mbc(ab, bc)  # Output the angle MBC
```
- **Common Problems**
    - **Problem**: Confusion between different trigonometric functions.
        - **Solution**: Use the atan2 function, which correctly handles the division of lengths and returns the angle in radians.

    - **Problem**: Incorrect conversion from radians to degrees.
        - **Solution**: Use the math.degrees function to accurately convert radians to degrees.
- **Additional Notes**
    - Mathematical Insight: The atan2(y, x) function returns the angle θ in radians between the x-axis and the line from the origin to the point (x, y). In this problem, y=AB and x=BC.

    - Edge Cases: Handle cases where sides AB and BC are very close in value, which might lead to rounding issues when converting to degrees.
    - Use Cases: This problem is useful for practicing trigonometry, specifically the use of arctangent in finding angles within a right-angled triangle.


## Find the Runner-Up Score!
**Definition**: Finding the runner-up score involves identifying the second highest unique score in a list of scores.

- **Approach**:

    - Remove Duplicate Scores: Convert the list of scores to a set to remove duplicates.
    - Find Unique Scores: Convert the set back to a sorted list.
    Identify Runner-Up: Retrieve the second highest score from the sorted list.
- **Example**:

```python
def find_runner_up(scores):
    unique_scores = list(set(scores))  # Remove duplicates
    unique_scores.sort()  # Sort the unique scores in ascending order
    return unique_scores[-2]  # Return the second last element (runner-up)

``` 
- Example:
```python
scores = [2, 3, 6, 6, 5]
print(find_runner_up(scores))  # Output: 5
```
- **Steps**:

Input: A list of integers representing scores.
Process:
Convert the list to a set to eliminate duplicates.
Convert the set to a list and sort it.
Access the second last element of the sorted list to get the runner-up score.
Output: The runner-up score.
- **Common Problems**:

    - **Problem**: The list might not contain enough unique scores to determine a runner-up.

        - **Solution**: Check if there are at least two unique scores before attempting to find the runner-up.
    - **Problem**: Handling cases where all scores are the same.

        - **Solution**: Ensure that the list contains more than one unique score. If not, return a message indicating that there is no runner-up.
## Finding the percentage
**Definition**: Calculating the percentage involves determining what portion one number represents of another number, expressed as a fraction of 100.

- **Formula**:

```python
percentage = (part / total) * 100
```
- **Example**:

```python
def calculate_percentage(part, total):
    if total == 0:
        raise ValueError("Total cannot be zero.")
    return (part / total) * 100

``` 
- Example:
```python
part = 45
total = 200
print(calculate_percentage(part, total))  # Output: 22.5
```
- **Steps**:

Input: Two numbers, part and total, where part is the portion of the total for which the percentage is to be calculated.
Process:
Divide the part by the total.
Multiply the result by 100 to get the percentage.
Output: The percentage value.
- **Common Problems**:

    - **Problem**: Division by zero if the total is zero.

        - **Solution**: Check if total is zero before performing the division and handle it appropriately (e.g., raise an exception or return a specific value).
    - **Problem**: Incorrect results due to improper input values (e.g., negative numbers).

        - **Solution**: Ensure that the input values are valid and handle any edge cases as needed.

## Integers Come In All Sizes

## Introduction to Sets
**Definition**: A set is an unordered collection of unique elements in Python. Sets are useful for storing distinct items and performing mathematical operations such as union, intersection, and difference.

- **Key Characteristics**:

    - Unordered: Sets do not maintain any specific order of elements.
    - Unique Elements: Duplicate elements are automatically removed.
    - Mutable: Sets can be modified after creation, but the elements themselves must be immutable.
- **Creating a Set**:

```python
# Creating an empty set
empty_set = set()

# Creating a set with initial elements
fruits = {"apple", "banana", "cherry"}
```
- **Common Set Operations**:

    - Add an Element:
    ```python
    fruits.add("orange")
    ```
    - Remove an Element:
    ```python
    fruits.remove("banana")  # Raises KeyError if element not found
    fruits.discard("banana") # Does not raise an error if element not found
    ```
    - Check Membership:
    ```python
    "apple" in fruits  # Output: True
    ```
    - Union of Sets:
    ```python
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    union_set = set1 | set2  # Output: {1, 2, 3, 4, 5}
    ```
    - Intersection of Sets:
    ```python
    intersection_set = set1 & set2  # Output: {3}
    ```
    - Difference of Sets:
    ```python
    difference_set = set1 - set2  # Output: {1, 2}
    ```
    - Symmetric Difference:
    ```python
    symmetric_diff_set = set1 ^ set2  # Output: {1, 2, 4, 5}
    ```
- **Examples**:

```python
# Creating a set
numbers = {1, 2, 3, 4, 5}
print(numbers)  # Output: {1, 2, 3, 4, 5}

# Adding an element
numbers.add(6)
print(numbers)  # Output: {1, 2, 3, 4, 5, 6}

# Removing an element
numbers.remove(4)
print(numbers)  # Output: {1, 2, 3, 5, 6}

# Checking membership
print(3 in numbers)  # Output: True

# Union
even_numbers = {2, 4, 6, 8}
all_numbers = numbers | even_numbers
print(all_numbers)  # Output: {1, 2, 3, 5, 6, 8}

# Intersection
common_numbers = numbers & even_numbers
print(common_numbers)  # Output: {6, 2}

# Difference
unique_numbers = numbers - even_numbers
print(unique_numbers)  # Output: {1, 3, 5}
```
- **Common Problems**:

    - **Problem**: Trying to add mutable elements (like lists) to a set.

        - **Solution**: Ensure that all elements in a set are immutable types (e.g., integers, strings, tuples).
    - **Problem**: Confusion between sets and lists, particularly regarding order and duplicates.

        - **Solution**: Remember that sets are unordered and do not allow duplicate elements, unlike lists.
## itertools.combinations()
**Definition**: The itertools.combinations() function returns all possible combinations of a specified length from the input iterable, without repeating elements. The combinations are produced in lexicographical order.

- **Syntax**:

```python
itertools.combinations(iterable, r)
```
    - iterable: The input iterable (e.g., list, string) from which combinations are generated.
    - r: The length of each combination.
    - Returns: An iterator that produces tuples containing all possible combinations of the specified length.

- **Examples**:

```python
import itertools

# Example 1: Combinations of length 2 from a list
items = [1, 2, 3]
comb = list(itertools.combinations(items, 2))
print(comb)  # Output: [(1, 2), (1, 3), (2, 3)]

# Example 2: Combinations of length 3 from a string
chars = 'ABC'
comb = list(itertools.combinations(chars, 2))
print(comb)  # Output: [('A', 'B'), ('A', 'C'), ('B', 'C')]

# Example 3: Combinations of length 1 from a set
elements = {1, 2, 3, 4}
comb = list(itertools.combinations(elements, 1))
print(comb)  # Output: [(1,), (2,), (3,), (4,)]
```
- **Use Cases**:

    - Generating combinations of items for testing or evaluation.
    - Creating combinations of elements for algorithms that require combinatorial analysis.
    - Generating possible selections or subsets from a dataset.
- **Common Problems**:

    - **Problem**: Misunderstanding the difference between combinations and permutations.

        - **Solution**: Remember that combinations do not consider order, whereas permutations do. Use itertools.permutations() for permutations.
    - **Problem**: Handling large iterables can be memory-intensive.

        - **Solution**: Use the iterator returned by itertools.combinations() directly rather than converting it to a list if dealing with very large datasets.
## itertools.combinations_with_replacement()
**Definition**: The itertools.combinations_with_replacement() function returns all possible combinations of a specified length from the input iterable, allowing for repeated elements. Each combination is produced in lexicographical order.

- **Syntax**:

```python
itertools.combinations_with_replacement(iterable, r)
```
    - iterable: The input iterable (e.g., list, string) from which combinations are generated.
    - r: The length of each combination.
    - Returns: An iterator that produces tuples containing all possible combinations of the specified length, allowing elements to repeat.

- **Examples**:

```python
import itertools

# Example 1: Combinations with replacement of length 2 from a list
items = [1, 2, 3]
comb = list(itertools.combinations_with_replacement(items, 2))
print(comb)  # Output: [(1, 1), (1, 2), (1, 3), (2, 2), (2, 3), (3, 3)]

# Example 2: Combinations with replacement of length 2 from a string
chars = 'AB'
comb = list(itertools.combinations_with_replacement(chars, 2))
print(comb)  # Output: [('A', 'A'), ('A', 'B'), ('B', 'B')]

# Example 3: Combinations with replacement of length 3 from a set
elements = {1, 2}
comb = list(itertools.combinations_with_replacement(elements, 3))
print(comb)  # Output: [(1, 1, 1), (1, 1, 2), (1, 2, 2), (2, 2, 2)]
```
- **Use Cases**:

    - Generating combinations where repetition of elements is allowed, such as in scenarios involving multi-choice problems or resource allocation.
    - Creating possible combinations for simulation or testing purposes where duplicate values are acceptable.
    - Analyzing combinatorial problems where repetition is part of the constraints.
- **Common Problems**:

    - **Problem**: Misunderstanding the difference between combinations with replacement and combinations without replacement.

        - **Solution**: Remember that combinations with replacement allow elements to appear more than once in each combination, unlike combinations without replacement which do not allow duplicates.
    - **Problem**: Handling large iterables with replacement can lead to many combinations.

        - **Solution**: Be cautious with the size of the input iterable and combination length to avoid excessive computation and memory usage.
## itertools.permutations()
**Definition**: The itertools.permutations() function returns all possible permutations of a specified length from the input iterable. A permutation is a rearrangement of elements, and each permutation is produced in lexicographical order if the input iterable is sorted.

- **Syntax**:

```python
itertools.permutations(iterable, r=None)
```
    - iterable: The input iterable (e.g., list, string) from which permutations are generated.
    - r: The length of each permutation. If r is not specified or is None, the length of the permutation is the same as the length of the iterable.
    - Returns: An iterator that produces tuples containing all possible permutations of the specified length.

- **Examples**:

```python
import itertools

# Example 1: Permutations of length 2 from a list
items = [1, 2, 3]
perm = list(itertools.permutations(items, 2))
print(perm)  # Output: [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# Example 2: Permutations of full length from a string
chars = 'AB'
perm = list(itertools.permutations(chars))
print(perm)  # Output: [('A', 'B'), ('B', 'A')]

# Example 3: Permutations of length 3 from a set
elements = {1, 2, 3}
perm = list(itertools.permutations(elements, 3))
print(perm)  # Output: [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]
```
- **Use Cases**:

    - Generating all possible orders or arrangements of items, useful in scenarios like scheduling, solving puzzles, or generating test cases.
    - Analyzing permutations in combinatorial problems where order matters.
    - Creating permutations of items for use in algorithms or optimization problems.
- **Common Problems**:

    - **Problem**: Large number of permutations when the iterable or permutation length is large, leading to high memory usage.

        - **Solution**: Be cautious with large input sizes and permutation lengths. Consider using the iterator directly without converting it to a list if dealing with large datasets.
    - **Problem**: Confusing permutations with combinations.

        - **Solution**: Remember that permutations consider order, while combinations do not. Use itertools.combinations() for combinations if order is not important.
## itertools.product()
**Definition**: The itertools.product() function computes the Cartesian product of input iterables. This means it returns all possible ordered pairs (or tuples) where each element from the Cartesian product is a combination of one element from each of the input iterables.

- **Syntax**:

```python
itertools.product(*iterables, repeat=1)
```
    - iterables: One or more input iterables whose Cartesian product is to be computed.
    - repeat: Number of repetitions of the Cartesian product for each iterable. The default value is 1.
    - Returns: An iterator that produces tuples containing the Cartesian product of the input iterables.

- **Examples**:

```python
import itertools

# Example 1: Cartesian product of two lists
list1 = [1, 2]
list2 = ['A', 'B']
prod = list(itertools.product(list1, list2))
print(prod)  # Output: [(1, 'A'), (1, 'B'), (2, 'A'), (2, 'B')]

# Example 2: Cartesian product with repetition
chars = 'AB'
prod = list(itertools.product(chars, repeat=2))
print(prod)  # Output: [('A', 'A'), ('A', 'B'), ('B', 'A'), ('B', 'B')]

# Example 3: Cartesian product of multiple iterables
nums = [1, 2]
letters = ['A', 'B']
colors = ['Red', 'Blue']
prod = list(itertools.product(nums, letters, colors))
print(prod)  # Output: [(1, 'A', 'Red'), (1, 'A', 'Blue'), (1, 'B', 'Red'), (1, 'B', 'Blue'), (2, 'A', 'Red'), (2, 'A', 'Blue'), (2, 'B', 'Red'), (2, 'B', 'Blue')]
```
- **Use Cases**:

    - Generating all possible combinations of items from multiple sets, useful in scenarios like product configuration or combinatorial testing.
    - Creating test cases where all possible combinations need to be evaluated.
    - Analyzing complex multi-dimensional datasets or problems where Cartesian products are involved.
- **Common Problems**:

    - **Problem**: Large number of products can result in excessive memory usage.

        - **Solution**: Be cautious with the number of input iterables and their sizes. Use the iterator returned by itertools.product() directly to avoid excessive memory usage.
    - **Problem**: Confusing Cartesian product with other combinatorial functions.

        - **Solution**: Understand that Cartesian product generates combinations with all possible pairs of elements, while other functions like itertools.combinations() or itertools.permutations() generate combinations or permutations with specific constraints.
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
**Definition**: A list is a built-in data structure in Python that holds an ordered collection of items. Lists are mutable, meaning their elements can be modified after creation, and they can contain elements of different data types.

- **Creating a List**:

```python
# Creating an empty list
empty_list = []

# Creating a list with initial elements
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "apple", 3.14, True]
```
- **Common List Operations**:

    - Accessing Elements:

    ```python
    first_element = numbers[0]  # Output: 1
    last_element = numbers[-1]  # Output: 5
    ```
    - Slicing:

    ```python
    sublist = numbers[1:4]  # Output: [2, 3, 4]
    ```
    - Adding Elements:

    ```python
    numbers.append(6)  # Adds 6 to the end of the list
    numbers.insert(2, 2.5)  # Inserts 2.5 at index 2
    ```
    - Removing Elements:

    ```python
    numbers.remove(2)  # Removes the first occurrence of 2
    del numbers[1]     # Deletes element at index 1
    ```
    - Finding Elements:

    ```python
    index_of_3 = numbers.index(3)  # Output: index of 3 in the list
    ```
    - List Length:

    ```python
    length = len(numbers)  # Output: Number of elements in the list
    ```
    - Iterating Over a List:

    ```python
    for item in numbers:
        print(item)
    ```
- **Examples**:

```python
# Creating and modifying a list
fruits = ["apple", "banana", "cherry"]
fruits.append("date")
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'date']

# Slicing a list
sliced_fruits = fruits[1:3]
print(sliced_fruits)  # Output: ['blueberry', 'cherry']
```
- **Use Cases**:

    - Storing and managing ordered collections of items.
    - Implementing various algorithms and data processing tasks.
    - Creating and manipulating collections of mixed data types.
- **Common Problems**:

    - **Problem**: IndexError when accessing elements out of the valid range.
        - **Solution**: Ensure that indices are within the range of the list's length.

    - **Problem**: Modifying a list while iterating over it can cause unexpected behavior.
        - **Solution**: Iterate over a copy of the list or use list comprehensions for safe modifications.

    - **Problem**: Performance issues with large lists.

        - **Solution**: Use efficient list operations and consider alternative data structures if performance becomes a concern.
## Loops
**Definition**: Loops in Python allow you to execute a block of code repeatedly based on certain conditions. They are used to iterate over sequences, such as lists, tuples, or strings, and to automate repetitive tasks.

- **Types of Loops**:

    - **for Loop**:

        - Purpose: Iterates over a sequence (e.g., list, tuple, string) or any iterable object.

        - **Syntax**:

        ```python
        for item in iterable:
            # Code to execute
        ```
        - **Examples**:

        ```python
        # Example 1: Iterating over a list
        fruits = ["apple", "banana", "cherry"]
        for fruit in fruits:
            print(fruit)

        # Example 2: Iterating over a range of numbers
        for i in range(5):
            print(i)
        ```
    - **while Loop**:

        - Purpose: Repeats a block of code as long as a specified condition is true.

        - **Syntax**:

        ```python
        while condition:
            # Code to execute
        ```
        - **Examples**:

        ```python
        # Example 1: Basic while loop
        count = 0
        while count < 5:
            print(count)
            count += 1

        # Example 2: Infinite loop (use with caution)
        # while True:
        #     print("This will run forever")
        ```
- **Loop Control Statements**:

    - break: Exits the current loop and continues execution with the first statement following the loop.

    ```python
    for i in range(10):
        if i == 5:
            break
        print(i)
    ```
    - continue: Skips the rest of the code inside the current loop iteration and proceeds with the next iteration.

    ```python
    for i in range(10):
        if i % 2 == 0:
            continue
        print(i)  # Output: 1, 3, 5, 7, 9
    ```
    - else: Executes a block of code once when the loop terminates normally (without a break).

    ```python
    for i in range(5):
        print(i)
    else:
        print("Loop finished")
    ```
- **Nested Loops**:

    - Purpose: Using one loop inside another to perform more complex iterations.

    - **Syntax**:

    ```python
    for i in range(3):
        for j in range(2):
            print(i, j)
    ```
    - **Example**:

    ```python
    for i in range(2):
        for j in range(3):
            print(f"i={i}, j={j}")
    ```
- **Common Problems**:

    - **Problem**: Infinite loops that never terminate.

        - **Solution**: Ensure loop conditions are updated properly and include a way to break out of the loop.
    - **Problem**: Modifying the loop variable inside the loop body can lead to unexpected behavior.

        - **Solution**: Carefully manage loop variables and avoid unnecessary modifications inside the loop body.
    - **Problem**: Performance issues with nested loops, especially with large datasets.

        - **Solution**: Optimize the code by minimizing the number of iterations and considering alternative algorithms if necessary.

## Merge The Tools
**Definition**: Merging tools or techniques in Python are used to combine multiple sequences or collections into a single sequence. This can involve merging lists, tuples, sets, or dictionaries.

- **Merging Lists**:

    - Using the + Operator:

    ```python
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    merged_list = list1 + list2
    print(merged_list)  # Output: [1, 2, 3, 4, 5, 6]
    ```
    - Using extend() Method:

    ```python
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list1.extend(list2)
    print(list1)  # Output: [1, 2, 3, 4, 5, 6]
    ```
    - Using List Comprehensions:

    ```python
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    merged_list = [item for sublist in [list1, list2] for item in sublist]
    print(merged_list)  # Output: [1, 2, 3, 4, 5, 6]
    ```
- **Merging Tuples**:

    - Using the + Operator:

    ```python
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    merged_tuple = tuple1 + tuple2
    print(merged_tuple)  # Output: (1, 2, 3, 4, 5, 6)
    ```
    - Using Tuple Comprehensions (if needed):

    ```python
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    merged_tuple = tuple(item for subtuple in (tuple1, tuple2) for item in subtuple)
    print(merged_tuple)  # Output: (1, 2, 3, 4, 5, 6)
    ```
- **Merging Sets**:

    - Using the | Operator:

    ```python
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    merged_set = set1 | set2
    print(merged_set)  # Output: {1, 2, 3, 4, 5}
    ```
    - Using union() Method:

    ```python
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    merged_set = set1.union(set2)
    print(merged_set)  # Output: {1, 2, 3, 4, 5}
    ```
- **Merging Dictionaries**:

    - Using the update() Method:

    ```python
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    dict1.update(dict2)
    print(dict1)  # Output: {'a': 1, 'b': 3, 'c': 4}
    ```
    - Using Dictionary Unpacking (Python 3.5+):

    ```python
    dict1 = {'a': 1, 'b': 2}
    dict2 = {'b': 3, 'c': 4}
    merged_dict = {**dict1, **dict2}
    print(merged_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}
    ```
    - Using dict() Constructor with a List of Tuples:

    ```python
    dict1 = {'a': 1}
    dict2 = {'b': 2}
    merged_dict = dict(list(dict1.items()) + list(dict2.items()))
    print(merged_dict)  # Output: {'a': 1, 'b': 2}
    ```
- **Common Problems**:

    - **Problem**: Duplicate elements when merging sets.

        - **Solution**: Use sets to automatically handle duplicates, or manage duplicates manually if needed.
    - **Problem**: Key conflicts when merging dictionaries.

        - **Solution**: Decide on a strategy for handling conflicts, such as keeping the latest value or merging values.
    - **Problem**: Performance issues with large datasets.

        - **Solution**: Use efficient data structures and merging techniques to optimize performance.

## Mod Divmod

## Mutations
**Definition**: Mutation refers to the ability to modify or change the contents of a data structure after it has been created. In Python, some data structures are mutable, meaning their contents can be altered, while others are immutable, meaning their contents cannot be changed once they are created.

- **Mutable Data Structures**:

    - **Lists**:

        - Modifying Elements:

        ```python
        my_list = [1, 2, 3]
        my_list[1] = 4
        print(my_list)  # Output: [1, 4, 3]
        ```
        - Adding Elements:

        ```python
        my_list.append(5)
        print(my_list)  # Output: [1, 4, 3, 5]
        ```
        - Removing Elements:

        ```python
        my_list.remove(4)
        print(my_list)  # Output: [1, 3, 5]
        ```
    - **Dictionaries**:

        - Modifying Values:

        ```python
        my_dict = {'a': 1, 'b': 2}
        my_dict['b'] = 3
        print(my_dict)  # Output: {'a': 1, 'b': 3}
        ```
        - Adding Key-Value Pairs:

        ```python
        my_dict['c'] = 4
        print(my_dict)  # Output: {'a': 1, 'b': 3, 'c': 4}
        ```
        - Removing Key-Value Pairs:

        ```python
        del my_dict['a']
        print(my_dict)  # Output: {'b': 3, 'c': 4}
        ```
    - **Sets**:

        - Adding Elements:

        ```python
        my_set = {1, 2, 3}
        my_set.add(4)
        print(my_set)  # Output: {1, 2, 3, 4}
        ```
        - Removing Elements:

        ```python
        my_set.discard(2)
        print(my_set)  # Output: {1, 3, 4}
        111
- **Immutable Data Structures**:

    - **Tuples**:

        - Creating Tuples:

        ```python
        my_tuple = (1, 2, 3)
        ```
        - Attempting to Modify:

        ```python
        # This will raise an error
        my_tuple[1] = 4  # TypeError: 'tuple' object does not support item assignment
        ```
    - **Strings**:

        - Creating Strings:

        ```python
        my_string = "hello"
        ```
        - Attempting to Modify:

        ```python
        # This will raise an error
        my_string[1] = 'a'  # TypeError: 'str' object does not support item assignment
        ```
- **Common Problems**:

    - **Problem**: Unintended side effects when modifying mutable data structures.

        - **Solution**: Be mindful of how mutable objects are shared and modified, especially when passed to functions.
    - **Problem**: Confusion between mutable and immutable types leading to unexpected behavior.

        - **Solution**: Understand the differences between mutable and immutable types and use appropriate data structures based on your needs.
    - **Problem**: Performance issues with frequent mutations.

        - **Solution**: Optimize data structure choices and operations to minimize performance impacts.
## Nested Lists
**Definition**: A nested list is a list that contains other lists as its elements. This allows for the creation of complex data structures, such as matrices or tables, where each element can itself be a list.

- **Creating Nested Lists**:

```python
# Creating a nested list (2D list)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
```
- **Accessing Elements**:

    - Single Element:

    ```python
    first_element = matrix[0][0]  # Output: 1
    ```
    - Slicing:

    ```python
    row = matrix[1]  # Output: [4, 5, 6]
    column = [row[1] for row in matrix]  # Output: [2, 5, 8]
    ```
    - Modifying Elements:

    ```python
    matrix[1][2] = 10
    print(matrix)  # Output: [[1, 2, 3], [4, 5, 10], [7, 8, 9]]
    ```
- **Iterating Over Nested Lists**:

    - Using Nested Loops:

    ```python
    for row in matrix:
        for item in row:
            print(item, end=' ')
        print()
    ```
    - Using List Comprehensions:

    ```python
    flattened = [item for row in matrix for item in row]
    print(flattened)  # Output: [1, 2, 3, 4, 5, 10, 7, 8, 9]
    ```
- **Common Operations**:

    - Finding the Sum of All Elements:

    ```python
    total_sum = sum(item for row in matrix for item in row)
    print(total_sum)  # Output: 55
    ```
    - Transposing a Matrix:

    ```python
    transposed = list(zip(*matrix))
    print(transposed)  # Output: [(1, 4, 7), (2, 5, 8), (3, 10, 9)]
    ```
- **Common Problems**:

    - **Problem**: IndexErrors due to incorrect indexing.

        - **Solution**: Ensure that indices used for accessing nested elements are within the valid range.
    - **Problem**: Difficulty in managing deeply nested structures.

        - **Solution**: Consider flattening the list or using data structures designed for hierarchical data, like trees or dictionaries, if appropriate.
    - **Problem**: Performance issues with large nested lists.

        - **Solution**: Optimize data access patterns and consider using efficient data structures or algorithms for large datasets.

## No Idea!
**Problem Statement**: Given a list of integers and two sets of integers, count the number of integers in the list that are present in either of the two sets.

- **Input Format**:

    - The first line contains two integers, n and m, representing the number of integers in the list and the number of integers in the two sets, respectively.
    - The second line contains n space-separated integers, representing the list.
    - The third line contains m space-separated integers, representing the first set.
    - The fourth line contains m space-separated integers, representing the second set.
- **Output Format**:

    - Print the number of integers in the list that are present in either of the two sets.
- **Example**:

    - Input:
    ```
    9 3
    1 5 3 4 2 6 4 6 7
    1 2 3
    5 6 7
    ```
- **Output**:
```
11
```
- **Explanation**:

    - The integers in the list are: [1, 5, 3, 4, 2, 6, 4, 6, 7]
    - The first set is: {1, 2, 3}
    - The second set is: {5, 6, 7}
    - The integers from the list that are in the first set or the second set  - are: [1, 5, 3, 5, 6, 7, 6]
    - The total count of such integers is 11.
- **Solution** 


    - Read the Input:

        - Parse the integers n and m.
        - Parse the list of integers.
        - Parse the two sets of integers.
    - Convert Lists to Sets:

        - Convert the two sets of integers into set1 and set2.
    - Count Matching Elements:

        - Iterate through the list of integers.
        - Count how many of these integers are present in either set1 or set2.
    - Print the Result:

        - Output the count.
- **Python Code**:

```python
# Read input
n, m = map(int, input().split())
lst = list(map(int, input().split()))
set1 = set(map(int, input().split()))
set2 = set(map(int, input().split()))

# Initialize counter
count = 0

# Count the number of integers in the list that are in either set
for number in lst:
    if number in set1 or number in set2:
        count += 1

# Print the result
print(count)
```
- **Common Problems**:

    - **Problem**: Incorrectly counting duplicates.

        - **Solution**: Ensure that the count reflects all occurrences in the list that match the criteria.
    - **Problem**: Inefficient solution for large inputs.

        - **Solution**: Use set operations for fast membership tests and efficient counting.


## Polar Coordinates
**Definition**: The "Polar Coordinates" problem involves converting a complex number into its polar coordinate components: the magnitude (or modulus) and the phase angle (or argument). This problem helps you practice using Python’s complex number functions and understanding polar coordinate representation.

- **Problem Statement**
You are given a complex number z. Your task is to print the magnitude and phase angle of z in two separate lines.

- Input:
```
A single line containing a complex number z in the form of x + yj, where x and y are real numbers.
```
- Output:
```
Print the magnitude (modulus) of z.
Print the phase angle (argument) of z.
```
- **Example**
- Input:

```python
z = "1+2j"
```
- Output:

```python
2.23606797749979
1.1071487177940904
```
- **Solution**
    - Algorithm:

        - Parse the Input: Read the complex number.
        - Calculate Magnitude: Use abs() to compute the magnitude (modulus) of the complex number.
        - Calculate Phase Angle: Use cmath.phase() to compute the phase angle (argument) of the complex number.
        - Print Results: Print the magnitude on the first line and the phase angle on the second line.
- **Python Code**:
```python
import cmath

def polar_coordinates(z):
    magnitude = abs(z)
    phase_angle = cmath.phase(z)
    print(magnitude)
    print(phase_angle)

# Example usage
z = complex(input())  # Example input: "1+2j"
polar_coordinates(z)
```
- **Common Problems**
    - **Problem**: Incorrect parsing of the complex number.
        - **Solution**: Ensure that the input is correctly interpreted as a complex number using the complex() function.

    - **Problem**: Incorrect computation of the phase angle.
        - **Solution**: Use the cmath.phase() function to accurately calculate the phase angle.
- **Additional Notes**
    - Mathematical Concepts:
        Magnitude (Modulus): The distance from the origin to the point represented by the complex number in the complex plane. Calculated as sqrt(x^2 + y^2).
        Phase Angle (Argument): The angle between the positive real axis and the line representing the complex number in the complex plane.
    - Libraries: The cmath module in Python provides the necessary functions to work with complex numbers and compute their polar coordinates.
    - Performance: The solution operates in constant time, O(1), since it only involves basic mathematical operations.

## Power - Mod Power

## Print Function
**Definition**: The print() function in Python is used to output data to the console. It can handle various types of data, including strings, numbers, and more complex data structures.

- **Basic Syntax**:

```python
print(object, sep=' ', end='\n', file=sys.stdout, flush=False)
```
    - object: The item(s) to be printed. Multiple items can be separated by commas.
    - sep: String inserted between values (default is a space).
    - end: String appended after the last value (default is a newline character).
    - file: A file-like object where the output will be sent (default is sys.stdout).
    - flush: Whether to forcibly flush the stream (default is False).
- **Examples**:

    - Basic Printing:

        ```python
        print("Hello, World!")  # Output: Hello, World!
        ```
    - Printing Multiple Items:

        ```python
        print("The answer is", 42)  # Output: The answer is 42
        ```
    - Changing Separator:

        ```python
        print("Python", "Java", "C++", sep=", ")  # Output: Python, Java, C++
    - Changing End Character:

        ```python
        print("Hello", end=" ")
        print("World!")  # Output: Hello World!
        ```
    - Printing to a File:

        ```python
        with open('output.txt', 'w') as f:
            print("Hello, file!", file=f)
        ```
    - Flushing the Output Buffer:

        ```python
        import time
        print("Processing...", end="", flush=True)
        time.sleep(2)
        print(" Done!")
        ```
- **Common Use Cases**:

Debugging: Printing variable values and program states for debugging purposes.
User Interaction: Displaying messages to users in interactive programs.
Logging: Writing messages to files for logging and auditing.
- **Common Problems**:

    - **Problem**: Output not appearing as expected (e.g., missing newlines).

        - **Solution**: Check end and sep parameters to ensure correct formatting.
    - **Problem**: Outputting data to the wrong destination (e.g., a file instead of the console).

        - **Solution**: Verify the file parameter to ensure output is directed to the intended location.
    - **Problem**: Buffering issues in interactive environments.

        - **Solution**: Use flush=True to ensure immediate output.
## Python Division
**Definition**: Division in Python involves dividing one number by another. Python supports both integer and floating-point division, and the results differ based on the type of division performed.

- **Types of Division**:

    - **True Division (/)**:

        **Definition**: Returns the quotient as a floating-point number.
        - **Syntax**:
        ```python
        result = dividend / divisor
        ```
        - **Examples**:
        ```python
        # Example 1: True division with integers
        result = 7 / 3
        print(result)  # Output: 2.3333333333333335

        # Example 2: True division with floats
        result = 7.0 / 3
        print(result)  # Output: 2.3333333333333335
        ```
    - **Floor Division (//)**:

        **Definition**: Returns the quotient as an integer, discarding the fractional part.
        - **Syntax**:
        ```python
        result = dividend // divisor
        ```
        - **Examples**:
        ```python
        # Example 1: Floor division with integers
        result = 7 // 3
        print(result)  # Output: 2

        # Example 2: Floor division with floats
        result = 7.0 // 3
        print(result)  # Output: 2.0
        ```
- **Difference Between True Division and Floor Division**:

    - True Division (/) retains the decimal part, providing a floating-point result.
    - Floor Division (//) removes the decimal part, providing an integer result if both operands are integers, or a float result with zero decimal part if at least one operand is a float.
- **Common Use Cases**:

    - True Division: When you need a precise floating-point result.
    - Floor Division: When you need to get the integer part of the division result, such as in algorithms that require whole numbers.
- **Common Problems**:

    - **Problem**: Division by zero raises a ZeroDivisionError.
        - **Solution**: Always check if the divisor is zero before performing division.

    - **Problem**: Confusion between // and / leading to unexpected results.
        - **Solution**: Understand the difference and choose the appropriate operator based on whether you need integer or floating-point results.

    - **Problem**: Unexpected results with mixed integer and float operands.
        - **Solution**: Be mindful of operand types and the resulting type of the division operation.

## Python If-Else
**Definition**: if-else statements are used for decision-making in Python programs. They allow the execution of different blocks of code based on a condition.

- **Basic Syntax**:

```python
if condition:
    # Code to execute if condition is True
else:
    # Code to execute if condition is False
```
- **Examples**:

    - Simple if-else Statement:

    ```python
    x = 10
    if x > 5:
        print("x is greater than 5")
    else:
        print("x is not greater than 5")
    # Output: x is greater than 5
    ```
    - if-elif-else Statement:

    ```python
    x = 15
    if x < 10:
        print("x is less than 10")
    elif x == 10:
        print("x is equal to 10")
    else:
        print("x is greater than 10")
    # Output: x is greater than 10
    ```
    - Nested if-else Statement:

    ```python
    x = 20
    if x > 10:
        if x < 30:
            print("x is between 10 and 30")
        else:
            print("x is 30 or greater")
    else:
        print("x is 10 or less")
    # Output: x is between 10 and 30
    ```
- **Comparison Operators**:

| Operator | Meaning| 
|----------|--------|
|==:| Equal to|
|!=:| Not equal to|
|>: |Greater than|
|<: |Less than|
|>=:| Greater than or equal to|
|<=:| Less than or equal to|
- **Logical Operators**:

| Operator | Meaning                                 | 
|----------|-----------------------------------------|
|and:| Returns True if both conditions are true.     |
|or: | Returns True if at least one condition is true.|
|not:| Returns True if the condition is false.       |

- **Examples**:

```python
x = 10
y = 20
if x > 5 and y > 15:
    print("Both conditions are true")
else:
    print("At least one condition is false")
# Output: Both conditions are true

if not x < 5:
    print("x is not less than 5")
# Output: x is not less than 5
```
- **Common Use Cases**:

    - Decision Making: Executing code based on specific conditions.
    - Validation: Checking if input values meet certain criteria.
    - Branching Logic: Directing the flow of execution based on various conditions.
- **Common Problems**:

    - **Problem**: Incorrectly nesting if-else statements leading to logic errors.

        - **Solution**: Ensure proper indentation and logical flow when nesting statements.
    - **Problem**: Overlapping conditions in if-elif statements leading to unreachable code.

        - **Solution**: Ensure that conditions are mutually exclusive and correctly ordered.
    - **Problem**: Using == instead of is for comparison (and vice versa).

        - **Solution**: Use == for value comparison and is for identity comparison.
## Say Hello World With Python
**Definition**: The "Hello, World!" program is a simple program that outputs the string "Hello, World!" to the console. It is often used as a beginner's introduction to a new programming language.

- **Basic Syntax**:

```python
print("Hello, World!")
```
- **Example**:

```python
# Print "Hello, World!" to the console
print("Hello, World!")
```
- **Output**:
```
Hello, World!
```
- **Explanation**:

    - print(): The print() function in Python outputs the specified message to the console.
    - "Hello, World!": The string to be printed. Strings in Python are enclosed in double quotes (or single quotes).
- **Common Use Cases**:

    - Learning the Basics: Used to verify that the programming environment is set up correctly and to practice basic syntax.
    - Testing Output: Checking that output functions work as expected.
- **Common Problems**:

    - **Problem**: Forgetting to use quotes around the string.

        - **Solution**: Ensure that the string is enclosed in double or single quotes.
    - **Problem**: Syntax errors due to incorrect use of the print() function.

        - **Solution**: Verify that the print() function is used correctly with parentheses and the string as its argument.
    - **Problem**: Code not producing output in some IDEs or text editors.

        - **Solution**: Ensure that you are running the script in an environment where the output can be displayed, such as a terminal or an IDE with a console.
## Set .add().
**Definition**: The set.add() method is used to add a single element to a set. If the element is already present in the set, it will not be added again, as sets do not allow duplicate elements.

- **Syntax**:

```python
set.add(element)
```
    - element: The item to be added to the set.
- **Examples**:

    - Basic Usage:

    ```python
    # Create a set
    my_set = {1, 2, 3}

    # Add an element to the set
    my_set.add(4)
    print(my_set)  # Output: {1, 2, 3, 4}
    ```
    - Adding Duplicate Elements:

    ```python
    my_set = {1, 2, 3}
    my_set.add(2)
    print(my_set)  # Output: {1, 2, 3}
    ```
    -- Adding Different Data Types:

    ```python
    my_set = {1, 2, 3}
    my_set.add("hello")
    print(my_set)  # Output: {1, 2, 3, 'hello'}
    ```
- **Common Use Cases**:

    - Building Sets: Adding elements to a set dynamically.
    - Ensuring Uniqueness: Using the set.add() method helps maintain the uniqueness of elements in a set.
- **Common Problems**:

    - **Problem**: Trying to add a mutable type (like a list) to a set.
        - **Solution**: Only immutable types (e.g., numbers, strings, tuples) can be added to a set. Use a tuple or another immutable type instead of a list.

    - **Problem**: Misunderstanding the behavior of sets with duplicate elements.
        - **Solution**: Understand that sets automatically handle duplicates and will not add an element if it is already present.

    - **Problem**: Attempting to use add() with non-set data types.
        - **Solution**: Ensure that you are calling add() on a set object.

## Set .difference() Operation
**Definition**: The set.difference() method returns a new set containing elements that are present in the calling set but not in the specified sets. It effectively computes the difference between two or more sets.

- **Syntax**:

```python
set.difference(*other_sets)
```
- other_sets: One or more sets to compare against. The method will return elements that are in the calling set but not in any of these sets.
- **Examples**:

    - Basic Usage:

    ```python
    # Define two sets
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7}

    # Find elements in set1 that are not in set2
    difference = set1.difference(set2)
    print(difference)  # Output: {1, 2, 3}
    ```
    - Multiple Sets:

    ```python
    # Define three sets
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7}
    set3 = {7, 8, 9}

    # Find elements in set1 that are not in set2 and set3
    difference = set1.difference(set2, set3)
    print(difference)  # Output: {1, 2, 3}
    ```
    - Empty Difference:

    ```python
    set1 = {1, 2, 3}
    set2 = {1, 2, 3}

    # Find elements in set1 that are not in set2
    difference = set1.difference(set2)
    print(difference)  # Output: set() (empty set)
    ```
- **Common Use Cases**:

    - Filtering: Finding elements that are unique to one set and not in others.
    - Set Operations: Performing difference operations in set theory and data analysis.
- **Common Problems**:

    - **Problem**: Passing non-set data types as arguments.

        - **Solution**: Ensure that all arguments to difference() are sets.
    - **Problem**: Misunderstanding that difference() does not modify the original set.

        - **Solution**: Note that difference() returns a new set and does not alter the calling set.
    - **Problem**: Confusion between difference() and difference_update().

        - **Solution**: Understand that difference() returns a new set while difference_update() modifies the calling set in place.
## Set .discard(), .remove() & .pop()
1. **set.discard() Method**:

    - **Definition**: The set.discard() method removes a specified element from the set if it exists. Unlike set.remove(), it does not raise an error if the element is not found.

    - **Syntax**:

    ```python
    set.discard(element)
    ```
        - element: The item to be removed from the set.
    - **Examples**:

    ```python
    # Create a set
    my_set = {1, 2, 3, 4}

    # Remove an element (no error if element is not found)
    my_set.discard(3)
    print(my_set)  # Output: {1, 2, 4}

    # Discard an element not in the set (no error)
    my_set.discard(5)
    print(my_set)  # Output: {1, 2, 4}
    ```
    - **Common Use Cases**:

        - Safe Removal: Removing an element without risking an error if the element does not exist.
    - **Common Problems**:

        - **Problem**: Misunderstanding that discard() does not raise an error if the element is missing.
            - **Solution**: Use discard() when you want to avoid handling potential errors from non-existing elements.
2. **set.remove() Method**:

    **Definition**: The set.remove() method removes a specified element from the set. If the element is not present, it raises a KeyError.

    - **Syntax**:

    ```python
    set.remove(element)
    ```
        - element: The item to be removed from the set.
    - **Examples**:

    ```python
    # Create a set
    my_set = {1, 2, 3, 4}

    # Remove an element (raises KeyError if element is not found)
    my_set.remove(3)
    print(my_set)  # Output: {1, 2, 4}

    # Attempt to remove an element not in the set
    try:
        my_set.remove(5)
    except KeyError:
        print("Element not found")
    # Output: Element not found
    ```
    - **Common Use Cases**:

    Error Handling: Removing an element with explicit error handling if the element is absent.
    - **Common Problems**:

        - **Problem**: Attempting to remove an element that does not exist raises an error.
            - **Solution**: Handle potential KeyError exceptions or use discard() if no error is preferred.
3. **set.pop() Method**:

    **Definition**: The set.pop() method removes and returns an arbitrary element from the set. Since sets are unordered, there is no guarantee of which element will be removed.

    - **Syntax**:

    ```python
    element = set.pop()
    ```
        - element: The item removed from the set (returned by the method).
    - **Examples**:

    ```python
    # Create a set
    my_set = {1, 2, 3, 4}

    # Remove and return an arbitrary element
    element = my_set.pop()
    print(element)  # Output: (an arbitrary element, e.g., 1)
    print(my_set)   # Output: Set with the remaining elements

    # Attempt to pop from an empty set
    empty_set = set()
    try:
        empty_set.pop()
    except KeyError:
        print("Set is empty")
    # Output: Set is empty
    ```
    - **Common Use Cases**:

    Arbitrary Removal: Removing an element when the specific element to be removed is not known.
    - **Common Problems**:

        - **Problem**: Popping from an empty set raises a KeyError.
            - **Solution**: Check if the set is empty before using pop().

## Set .intersection() Operation
**Definition**: The set.intersection() method returns a new set containing elements that are common to all specified sets. It effectively computes the intersection of two or more sets.

- **Syntax**:

```python
set.intersection(*other_sets)
```
- other_sets: One or more sets to compare against. The method will return elements that are present in the calling set and all other specified sets.
- **Examples**:

    - Basic Usage:

    ```python
    # Define two sets
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7}

    # Find elements common to both set1 and set2
    intersection = set1.intersection(set2)
    print(intersection)  # Output: {4, 5}
    ```
    - Multiple Sets:

    ```python
    # Define three sets
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7}
    set3 = {5, 6, 7, 8}

    # Find elements common to set1, set2, and set3
    intersection = set1.intersection(set2, set3)
    print(intersection)  # Output: {5}
    ```
    - Empty Intersection:

    ```python
    # Define sets with no common elements
    set1 = {1, 2, 3}
    set2 = {4, 5, 6}

    # Find elements common to both sets
    intersection = set1.intersection(set2)
    print(intersection)  # Output: set() (empty set)
    ```
- **Common Use Cases**:

    - Finding Common Elements: Identifying elements that are shared among multiple sets.
    - Set Operations: Performing intersection operations in data analysis and set theory.
- **Common Problems**:

    - **Problem**: Passing non-set data types as arguments.

        - **Solution**: Ensure that all arguments to intersection() are sets.
    - **Problem**: Misunderstanding that intersection() does not modify the original sets.

        - **Solution**: Note that intersection() returns a new set and does not alter the calling sets.
    - **Problem**: Confusion between intersection() and intersection_update().

        - **Solution**: Understand that intersection() returns a new set while intersection_update() modifies the calling set in place.
## Set .symmetric_difference() Operation
**Definition**: The set.symmetric_difference() method returns a new set containing elements that are in either of the sets but not in their intersection. In other words, it returns the elements that are unique to each set.

- **Syntax**:

```python
set.symmetric_difference(other_set)
```
    - other_set: The set to compare against. The method will return elements that are in either the calling set or the other_set, but not in both.
- **Examples**:

    - Basic Usage:

    ```python
    # Define two sets
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7}

    # Find elements that are in either set1 or set2, but not in both
    symmetric_difference = set1.symmetric_difference(set2)
    print(symmetric_difference)  # Output: {1, 2, 6, 7}
    ```
    - Multiple Sets:

    ```python
    # Define three sets
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7}
    set3 = {5, 6, 7, 8}

    # Find elements that are unique to set1, set2, and set3
    symmetric_difference = set1.symmetric_difference(set2).symmetric_difference(set3)
    print(symmetric_difference)  # Output: {1, 2, 8}
    ```
    - Empty Symmetric Difference:

    ```python
    # Define sets with the same elements
    set1 = {1, 2, 3}
    set2 = {1, 2, 3}

    # Find elements that are in either set1 or set2, but not in both
    symmetric_difference = set1.symmetric_difference(set2)
    print(symmetric_difference)  # Output: set() (empty set)
    ```
- **Common Use Cases**:

    - Identifying Unique Elements: Finding elements that are unique to each set, useful in various data analysis scenarios.
    - Set Operations: Performing symmetric difference operations in set theory and data manipulation.
- **Common Problems**:

    - **Problem**: Passing non-set data types as arguments.

        - **Solution**: Ensure that the argument to symmetric_difference() is a set.
    - **Problem**: Misunderstanding that symmetric_difference() does not modify the original sets.

        - **Solution**: Note that symmetric_difference() returns a new set and does not alter the calling sets.
    - **Problem**: Confusion between symmetric_difference() and symmetric_difference_update().

        - **Solution**: Understand that symmetric_difference() returns a new set while symmetric_difference_update() modifies the calling set in place.
## Set .union() Operation
**Definition**: The set.union() method returns a new set containing all elements from the calling set and the specified sets. It effectively combines all unique elements from the given sets.

- **Syntax**:

```python
set.union(*other_sets)
```
- other_sets: One or more sets to be combined with the calling set. The method will return a new set containing all unique elements from the calling set and all other specified sets.
- **Examples**:

    Basic Usage:

    ```python
    # Define two sets
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}

    # Find the union of set1 and set2
    union = set1.union(set2)
    print(union)  # Output: {1, 2, 3, 4, 5, 6}
    ```
    - Multiple Sets:

    ```python
    # Define three sets
    set1 = {1, 2, 3}
    set2 = {3, 4, 5}
    set3 = {5, 6, 7}

    # Find the union of set1, set2, and set3
    union = set1.union(set2, set3)
    print(union)  # Output: {1, 2, 3, 4, 5, 6, 7}
    ```
    - Union with an Empty Set:

    ```python
    # Define a set and an empty set
    set1 = {1, 2, 3}
    empty_set = set()

    # Find the union of set1 and an empty set
    union = set1.union(empty_set)
    print(union)  # Output: {1, 2, 3}
    ```
- **Common Use Cases**:

    - Combining Sets: Merging multiple sets into a single set containing all unique elements.
    - Data Aggregation: Collecting unique items from different datasets or collections.
- **Common Problems**:

    - **Problem**: Passing non-set data types as arguments.

        - **Solution**: Ensure that all arguments to union() are sets.
    - **Problem**: Misunderstanding that union() does not modify the original sets.

        - **Solution**: Note that union() returns a new set and does not alter the calling sets.
    - **Problem**: Confusion between union() and update().

        - **Solution**: Understand that union() returns a new set while update() modifies the calling set in place.
## Set Mutations
**Definition**: Set mutations refer to methods that modify the set in place, such as adding, removing, or updating elements. These operations change the state of the original set rather than creating a new set.

1. **set.add()**:
    **Definition**: Adds a single element to the set. If the element is already present, it does nothing.

    - **Syntax**:

    ```python
    set.add(element)
    ```
    - **Example**:

    ```python
    my_set = {1, 2, 3}
    my_set.add(4)
    print(my_set)  # Output: {1, 2, 3, 4}
    ```
2. **set.remove()**:
    **Definition**: Removes a specified element from the set. Raises a KeyError if the element is not found.

    - **Syntax**:

    ```python
    set.remove(element)
    ```
    - **Example**:

    ```python
    my_set = {1, 2, 3, 4}
    my_set.remove(3)
    print(my_set)  # Output: {1, 2, 4}
    ```
    - **Common Problems**:

        - **Problem**: Attempting to remove an element that does not exist.
            - **Solution**: Use discard() if you want to avoid handling exceptions.
3. **set.discard()**:
    **Definition**: Removes a specified element from the set if it exists. Does nothing if the element is not found, unlike remove().

    - **Syntax**:

    ```python
    set.discard(element)
    ```
    - **Example**:

    ```python
    my_set = {1, 2, 3, 4}
    my_set.discard(3)
    print(my_set)  # Output: {1, 2, 4}
    ```
    - **Common Problems**:

        - **Problem**: No effect if the element is missing.
            - **Solution**: Use discard() when you want to avoid exceptions for non-existent elements.
4. **set.pop()**:
    **Definition**: Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.

    - **Syntax**:

    ```python
    element = set.pop()
    ```
    - **Example**:

    ```python
    my_set = {1, 2, 3}
    element = my_set.pop()
    print(element)  # Output: (an arbitrary element, e.g., 1)
    print(my_set)   # Output: Set with the remaining elements
    ```
    - **Common Problems**:

        - **Problem**: Attempting to pop from an empty set.
            - **Solution**: Check if the set is empty before using pop().
5. **set.update()**:
    **Definition**: Updates the set with elements from one or more other sets or iterables. Adds all unique elements from the provided arguments.

    - **Syntax**:

    ```python
    set.update(*other_sets_or_iterables)
    ```
    - **Example**:

    ```python
    my_set = {1, 2, 3}
    my_set.update({3, 4, 5})
    print(my_set)  # Output: {1, 2, 3, 4, 5}
    ```
6. **set.intersection_update()**:
    **Definition**: Updates the set to keep only elements found in both the set and all specified sets.

    - **Syntax**:

    ```python
    set.intersection_update(*other_sets)
    ```
    - **Example**:

    ```python
    my_set = {1, 2, 3, 4}
    my_set.intersection_update({2, 3, 5})
    print(my_set)  # Output: {2, 3}
    ```
7. **set.difference_update()**:
    **Definition**: Updates the set to remove elements found in the specified sets.

    - **Syntax**:

    ```python
    set.difference_update(*other_sets)
    ```
    - **Example**:

    ```python
    my_set = {1, 2, 3, 4}
    my_set.difference_update({3, 4, 5})
    print(my_set)  # Output: {1, 2}
    ```
8. **set.symmetric_difference_update()**:
    **Definition**: Updates the set to keep only elements that are in either of the sets but not in their intersection.

    - **Syntax**:

    ```python
    set.symmetric_difference_update(other_set)
    ```
    - **Example**:

    ```python
    my_set = {1, 2, 3, 4}
    my_set.symmetric_difference_update({3, 4, 5, 6})
    print(my_set)  # Output: {1, 2, 5, 6}
    ```
## String Formatting
**Definition**: String formatting in Python refers to the techniques used to construct strings by embedding variables and expressions within string literals. There are several methods to achieve string formatting, including the % operator, str.format(), and f-strings (formatted string literals).

1. **% Operator (Old Style Formatting)**:
    **Definition**: This is an older method for formatting strings, similar to the printf-style formatting found in C.

    - **Syntax**:

    ```python
    "format_string" % (values)
    ```
    - format_string: A string containing format specifiers (e.g., %s, %d).
    values: Values to be inserted into the format specifiers.
    - **Examples**:

    ```python
    # Basic example
    name = "Alice"
    age = 30
    formatted_string = "Name: %s, Age: %d" % (name, age)
    print(formatted_string)  # Output: Name: Alice, Age: 30

    # Precision and width
    pi = 3.14159
    formatted_string = "Pi to two decimal places: %.2f" % pi
    print(formatted_string)  # Output: Pi to two decimal places: 3.14
    ```
    - **Common Problems**:

        - **Problem**: Limited formatting options and readability.
            - **Solution**: Consider using str.format() or f-strings for more complex formatting.
2. **str.format() Method**:
    **Definition**: The str.format() method provides a more flexible way to format strings compared to the % operator.

    - **Syntax**:

    ```python
    "format_string".format(values)
    ```
    - format_string: A string containing placeholders ({}) where values will be inserted.
    - values: Values to be inserted into the placeholders.
    - **Examples**:

    ```python
    # Basic example
    name = "Bob"
    age = 25
    formatted_string = "Name: {}, Age: {}".format(name, age)
    print(formatted_string)  # Output: Name: Bob, Age: 25

    # Using index and named placeholders
    formatted_string = "Name: {0}, Age: {1}. {0} is {1} years old.".format(name, age)
    print(formatted_string)  # Output: Name: Bob, Age: 25. Bob is 25 years old.

    # Formatting numbers
    pi = 3.14159
    formatted_string = "Pi to two decimal places: {:.2f}".format(pi)
    print(formatted_string)  # Output: Pi to two decimal places: 3.14
    ```
    - **Common Problems**:

        - **Problem**: Complexity increases with multiple placeholders and complex formatting.
            - **Solution**: Use f-strings for a more readable and modern approach.
3. **f-strings (Formatted String Literals) (Python 3.6+)**:
    **Definition**: F-strings provide a concise and readable way to format strings by embedding expressions inside curly braces {} within string literals.

    - **Syntax**:

    ```python
    f"format_string with {expression}"
    ```
    - format_string: A string literal prefixed with f.
    - expression: Any valid Python expression or variable.
    - **Examples**:

    ```python
    # Basic example
    name = "Carol"
    age = 22
    formatted_string = f"Name: {name}, Age: {age}"
    print(formatted_string)  # Output: Name: Carol, Age: 22

    # Using expressions
    pi = 3.14159
    formatted_string = f"Pi to two decimal places: {pi:.2f}"
    print(formatted_string)  # Output: Pi to two decimal places: 3.14

    # Evaluating expressions
    x = 5
    formatted_string = f"Five squared is {x**2}"
    print(formatted_string)  # Output: Five squared is 25
    ```
    - **Common Problems**:

        - **Problem**: F-strings are available only in Python 3.6 and later.
            - **Solution**: Use str.format() or % operator in earlier versions of Python.
## String Split and Join
**Definition**: String splitting and joining are operations used to manipulate and process strings. Splitting divides a string into a list of substrings based on a delimiter, while joining combines a list of strings into a single string with a specified separator.

1. **str.split()**:
    **Definition**: The str.split() method divides a string into a list of substrings based on a specified delimiter. If no delimiter is provided, it splits on whitespace by default.

    - **Syntax**:

    ```python
    str.split(separator, maxsplit)
    ```
    - separator (optional): The delimiter on which to split the string. If omitted, any whitespace is used.
    - maxsplit (optional): The maximum number of splits to perform. If omitted, all occurrences of the delimiter are used.
    - **Examples**:

    ```python
    # Basic example
    text = "apple,orange,banana"
    result = text.split(",")
    print(result)  # Output: ['apple', 'orange', 'banana']

    # Splitting on whitespace
    text = "This is a sentence."
    result = text.split()
    print(result)  # Output: ['This', 'is', 'a', 'sentence.']

    # Limiting splits
    text = "one two three four"
    result = text.split(" ", 2)
    print(result)  # Output: ['one', 'two', 'three four']
    ```
    - **Common Problems**:

        - **Problem**: Delimiter not found in the string.

            - **Solution**: Check if the delimiter is correctly specified or handle the resulting list if empty.
        - **Problem**: Unexpected whitespace handling.

            - **Solution**: Be aware of how split() treats whitespace when no delimiter is specified.
2. **str.join()**:
    **Definition**: The str.join() method combines a list of strings into a single string, with a specified separator between each element.

    - **Syntax**:

    ```python
    separator.join(iterable)
    ```
    - separator: The string that will be placed between elements of the iterable.
    - iterable: A sequence of strings to join into a single string.
    - **Examples**:

    ```python
    # Basic example
    words = ['apple', 'orange', 'banana']
    result = ", ".join(words)
    print(result)  # Output: 'apple, orange, banana'

    # Joining with no separator
    words = ['hello', 'world']
    result = "".join(words)
    print(result)  # Output: 'helloworld'

    # Joining with newline separator
    lines = ['first line', 'second line', 'third line']
    result = "\n".join(lines)
    print(result)  
    # - **Output**:
    # first line
    # second line
    # third line
    ```
    - **Common Problems**:

        - **Problem**: Trying to join non-string elements.

            - **Solution**: Ensure that all elements in the iterable are strings before using join().
        - **Problem**: Unexpected results when using separators.

            - **Solution**: Verify the separator and its intended placement between elements.
## String Validators
**Definition**: String validators are methods used to check if a string meets specific criteria, such as being alphanumeric, alphabetical, numeric, or having specific formatting requirements.

1. **str.isalnum()**:
    **Definition**: Returns True if all characters in the string are alphanumeric (i.e., letters and digits) and there is at least one character; otherwise, returns False.

    - **Syntax**:

    ```python
    str.isalnum()
    ```
    - **Examples**:

    ```python
    # Example with alphanumeric characters
    text = "abc123"
    result = text.isalnum()
    print(result)  # Output: True

    # Example with non-alphanumeric characters
    text = "abc 123"
    result = text.isalnum()
    print(result)  # Output: False
    ```
2. **str.isalpha()**:
    **Definition**: Returns True if all characters in the string are alphabetic and there is at least one character; otherwise, returns False.

    - **Syntax**:

    ```python
    str.isalpha()
    ```
    - **Examples**:

    ```python
    # Example with alphabetic characters
    text = "hello"
    result = text.isalpha()
    print(result)  # Output: True

    # Example with numeric characters
    text = "hello123"
    result = text.isalpha()
    print(result)  # Output: False
    ```
3. **str.isdigit()**:
    **Definition**: Returns True if all characters in the string are digits and there is at least one character; otherwise, returns False.

    - **Syntax**:

    ```python
    str.isdigit()
    ```
    - **Examples**:

    ```python
    # Example with digit characters
    text = "12345"
    result = text.isdigit()
    print(result)  # Output: True

    # Example with non-digit characters
    text = "123a5"
    result = text.isdigit()
    print(result)  # Output: False
    ```
4. **str.isspace()**:
    **Definition**: Returns True if all characters in the string are whitespace characters and there is at least one character; otherwise, returns False.

    - **Syntax**:

    ```python
    str.isspace()
    ```
    - **Examples**:

    ```python
    # Example with whitespace characters
    text = "    "
    result = text.isspace()
    print(result)  # Output: True

    # Example with mixed characters
    text = "  hello  "
    result = text.isspace()
    print(result)  # Output: False
    ```
5. **str.islower()**:
    **Definition**: Returns True if all characters in the string are lowercase letters and there is at least one character; otherwise, returns False.

    - **Syntax**:

    ```python
    str.islower()
    ```
    - **Examples**:

    ```python
    # Example with lowercase letters
    text = "hello"
    result = text.islower()
    print(result)  # Output: True

    # Example with uppercase letters
    text = "Hello"
    result = text.islower()
    print(result)  # Output: False
    ```
6. **str.isupper()**:
    **Definition**: Returns True if all characters in the string are uppercase letters and there is at least one character; otherwise, returns False.

    - **Syntax**:

    ```python
    str.isupper()
    ```
    - **Examples**:

    ```python
    # Example with uppercase letters
    text = "HELLO"
    result = text.isupper()
    print(result)  # Output: True

    # Example with mixed case letters
    text = "Hello"
    result = text.isupper()
    print(result)  # Output: False
    ```
7. **str.istitle()**:
    **Definition**: Returns True if the string is in title case (i.e., each word starts with an uppercase letter and all other letters are lowercase); otherwise, returns False.

    - **Syntax**:

    ```python
    str.istitle()
    ```
    - **Examples**:

    ```python
    # Example with title case
    text = "This Is A Title"
    result = text.istitle()
    print(result)  # Output: True

    # Example with non-title case
    text = "This is not a Title"
    result = text.istitle()
    print(result)  # Output: False
    ```
## sWAP cASE
**Definition**: The sWAP cASE problem involves converting all uppercase letters in a string to lowercase and all lowercase letters to uppercase. This transformation should be applied to each character in the string.

- **Problem Statement**:
Given a string, swap the case of each letter. That is, convert all uppercase letters to lowercase and all lowercase letters to uppercase.

- **Example**:
Input: "Hello World"

Output: "hELLO wORLD"

Input: "Python Programming"

Output: "pYTHON pROGRAMMING"

- **Solution**:
Method: Use the str.swapcase() method, which is a built-in Python method designed to swap the case of all letters in a string.

- **Syntax**:

```python
str.swapcase()
```
- **Example**:

```python
# Example 1
text = "Hello World"
result = text.swapcase()
print(result)  # Output: "hELLO wORLD"

# Example 2
text = "Python Programming"
result = text.swapcase()
print(result)  # Output: "pYTHON pROGRAMMING"
```
- **Common Problems**:
    - **Problem**: The input string contains non-alphabetic characters (e.g., digits, punctuation).

        - **Solution**: str.swapcase() handles non-alphabetic characters by leaving them unchanged, so no additional handling is required.
    - **Problem**: The input string is empty.

        - **Solution**: An empty string will return an empty string when swapcase() is applied.
- **Additional Notes**:
    - Performance: The str.swapcase() method is efficient and works in linear time relative to the length of the string.

    - Alternative: For custom cases or additional processing, you can use a list comprehension or a loop to manually swap cases:

        ```python
        def swap_case_custom(text):
            return ''.join(c.lower() if c.isupper() else c.upper() for c in text)

        ``` 
    - Example:
    ```python
        text = "Hello World"
        result = swap_case_custom(text)
        print(result)  # Output: "hELLO wORLD"
        ```

## Symmetric Difference
**Definition**: The symmetric difference between two sets is a set containing elements that are in either of the sets but not in their intersection. In other words, it includes elements that are in one of the sets but not in both.
- **Syntax**:
    - Using ^ Operator:

    ```python
    set1 ^ set2
    ```
    - Using set.symmetric_difference() Method:

    ```python
    set1.symmetric_difference(set2)
    ```
- **Examples**:
    - Basic Example:

        ```python
        # Define two sets
        set1 = {1, 2, 3, 4}
        set2 = {3, 4, 5, 6}

        # Calculate symmetric difference
        result = set1 ^ set2
        print(result)  # Output: {1, 2, 5, 6}

        # Using method
        result = set1.symmetric_difference(set2)
        print(result)  # Output: {1, 2, 5, 6}
        ```
    - Example with Strings:

        ```python
        # Define two sets of characters
        set1 = {'a', 'b', 'c', 'd'}
        set2 = {'c', 'd', 'e', 'f'}

        # Calculate symmetric difference
        result = set1 ^ set2
        print(result)  # Output: {'a', 'b', 'e', 'f'}

        # Using method
        result = set1.symmetric_difference(set2)
        print(result)  # Output: {'a', 'b', 'e', 'f'}
        ```
- **Common Problems**:
    - **Problem**: Incorrect results when the sets contain nested sets or mutable types.

        - **Solution**: Ensure that the sets only contain hashable types, as sets themselves cannot be elements of other sets.
    - **Problem**: Misunderstanding the difference between symmetric difference and other set operations like union or difference.

        - **Solution**: Understand the **Definition**: symmetric difference is the union of the sets minus their intersection.
- **Additional Notes**:
    - Performance: Symmetric difference operations are efficient, typically running in linear time relative to the number of elements in the sets.
- **Use Cases**: Useful in scenarios where you need to find elements that are unique to each set, such as in comparison tasks or when eliminating common elements.

## Text Alignment
**Definition**: Text alignment involves formatting strings so that they are aligned to the left, center, or right within a specified width. This can be achieved using various methods in Python.

1. **Using str.ljust(), str.rjust(), and str.center()**:
    
    **Definition**: These methods adjust the alignment of a string within a given width, padding it with specified characters if needed.

    - str.ljust(width, fillchar): Left-aligns the string within the given width, padding with fillchar (default is a space).

        - **Syntax**:

                ```python
                str.ljust(width, fillchar)
                ```
        - **Example**:

                ```python
                text = "Hello"
                result = text.ljust(10, '-')
                print(result)  # Output: 'Hello-----'
                ```
    - str.rjust(width, fillchar): Right-aligns the string within the given width, padding with fillchar (default is a space).

        - **Syntax**:

        ```python
        str.rjust(width, fillchar)
        ```
        - **Example**:

        ```python
        text = "Hello"
        result = text.rjust(10, '-')
        print(result)  # Output: '-----Hello'
        ```
    - str.center(width, fillchar): Centers the string within the given width, padding with fillchar (default is a space).

        - **Syntax**:

        ```python
        str.center(width, fillchar)
        ```
        - **Example**:

        ```python
        text = "Hello"
        result = text.center(10, '-')
        print(result)  # Output: '--Hello---'
        ```
2. **Using f-strings (Python 3.6+)**:
    **Definition**: F-strings allow for inline text alignment within formatted strings by using format specifiers.

    - **Syntax**:

    ```python
    f"{value:alignment_width}"
    ```
    - alignment_width: Specifies the width of the field and the alignment.
    - **Examples**:

    ```python
    # Left alignment
    text = "Hello"
    print(f"{text:<10}")  # Output: 'Hello     '

    # Right alignment
    text = "Hello"
    print(f"{text:>10}")  # Output: '     Hello'

    # Center alignment
    text = "Hello"
    print(f"{text:^10}")  # Output: '  Hello   '
    ```
3. **Using str.format()**:
    **Definition**: The str.format() method provides another way to format strings with alignment options.

    - **Syntax**:

    ```python
    "{value:alignment_width}"
    ```
    - alignment_width: Specifies the width and alignment of the field.
    - **Examples**:

    ```python
    # Left alignment
    text = "Hello"
    print("{:<10}".format(text))  # Output: 'Hello     '

    # Right alignment
    text = "Hello"
    print("{:>10}".format(text))  # Output: '     Hello'

    # Center alignment
    text = "Hello"
    print("{:^10}".format(text))  # Output: '  Hello   '
    ```
- **Common Problems**:
    - **Problem**: Alignment not working as expected with non-string data types.

        - **Solution**: Convert non-string types to strings before applying alignment.
    - **Problem**: Unexpected padding characters or widths.

        - **Solution**: Ensure that the width and padding characters are specified correctly according to the formatting method used.
- **Additional Notes**:
- Performance: Alignment methods are efficient and typically run in linear time relative to the string length.
- **Use Cases**: Text alignment is useful for creating neatly formatted outputs, such as in tables, reports, and user interfaces.

## Text Wrap
**Definition**: Text wrapping involves breaking a long string into multiple lines so that each line does not exceed a specified width. This is useful for formatting text in a readable way.

- **Using textwrap Module**:
    The textwrap module provides functions to format and wrap text.

    1. **textwrap.wrap()**:

    **Definition**: Wraps the input text into a list of lines, each of which is no longer than a given width.

    - **Syntax**:

    ```python
    import textwrap
    textwrap.wrap(text, width, **kwargs)
    ```
        - text: The input string to be wrapped.
        - width: The maximum width of each line.
    - **Examples**:

    ```python
    import textwrap

    text = "This is a long line of text that needs to be wrapped according to the specified width."
    wrapped_text = textwrap.wrap(text, width=20)
    print(wrapped_text)
    # Output: ['This is a long line', 'of text that needs', 'to be wrapped according', 'to the specified width.']
    ```
    2. textwrap.fill()

    **Definition**: Wraps the input text into a single string with line breaks, ensuring each line does not exceed the given width.

    - **Syntax**:

    ```python
    import textwrap
    textwrap.fill(text, width, **kwargs)
    ```
        - text: The input string to be wrapped.
        - width: The maximum width of each line.
    - **Examples**:

    ```python
    import textwrap

    text = "This is a long line of text that needs to be wrapped according to the specified width."
    filled_text = textwrap.fill(text, width=20)
    print(filled_text)
    # - **Output**:
    # This is a long line
    # of text that needs
    # to be wrapped according
    # to the specified width.
    ```
    3. textwrap.shorten()

    **Definition**: Shortens a string to fit within a given width, appending an ellipsis (...) if necessary.

    - **Syntax**:

    ```python
    import textwrap
    textwrap.shorten(text, width, **kwargs)
    ```
        - text: The input string to be shortened.
        - width: The maximum width of the shortened text.
    - **Examples**:

    ```python
    import textwrap

    text = "This is a long line of text that will be shortened."
    shortened_text = textwrap.shorten(text, width=30, placeholder="...")
    print(shortened_text)
    # Output: 'This is a long line of text...'
    ```
- **Common Problems**:
    - **Problem**: Lines are cut off in the middle of words.

        - **Solution**: Ensure the width is set to a value that avoids cutting words or use textwrap.wrap() for more control.
    - **Problem**: Text is not wrapped properly due to special characters or formatting.

        - **Solution**: Clean the text before wrapping if special characters are causing issues.
- **Additional Notes**:
Performance: Wrapping functions are efficient and typically handle text in linear time relative to its length.
- **Use Cases**: Useful for formatting text output, such as in console applications, reports, and text-based user interfaces.

## The Captain's Room
**Definition**: In a list where every element appears twice except for one unique element, find the unique element. This problem tests your ability to handle lists and understand how to identify unique items among duplicates.

- **Problem Statement**:
You are given a list of integers where every integer appears exactly twice, except for one integer which appears only once. Your task is to identify that unique integer.

- **Example**:
Input: [1, 2, 3, 2, 1]

Output: 3

Input: [4, 5, 6, 4, 5]

Output: 6

- **Solution**:
    - **Method 1: Using Set**:

        **Definition**: Use a set to track occurrences and identify the unique integer.

        - **Algorithm**:

        - Initialize an empty set.
        - Iterate through the list.
        - Add each item to the set if it is not already present, or remove it if it is.
        - The remaining item in the set is the unique integer.
        - **Python Code**:

        ```python
        def find_unique_room(rooms):
            unique = set()
            for room in rooms:
                if room in unique:
                    unique.remove(room)
                else:
                    unique.add(room)
            return unique.pop()
        

        ``` 
    - Example:
    ```python
        rooms = [1, 2, 3, 2, 1]
        print(find_unique_room(rooms))  # Output: 3
        ```
    - **Method 2: Using XOR Operation**:

        **Definition**: Use the XOR bitwise operation, which has the property that a ^ a = 0 and a ^ 0 = a. Thus, XOR-ing all elements will cancel out the duplicates and leave the unique element.

        - **Algorithm**:

        - Initialize a variable to 0.
        - XOR each item in the list with the variable.
        - The result will be the unique integer.
        
        - **Python Code**:

        ```python
        def find_unique_room(rooms):
            unique = 0
            for room in rooms:
                unique ^= room
            return unique

        ``` 
        - Example:
        ```python
        rooms = [1, 2, 3, 2, 1]
        print(find_unique_room(rooms))  # Output: 3
        ```
- **Common Problems**:
    - **Problem**: Handling an empty list or a list where no integer appears exactly twice.

        - **Solution**: Ensure that the problem constraints are met before applying the solution. For an empty list or invalid input, handle appropriately with error messages or defaults.
    - **Problem**: Performance issues with very large lists.

        - **Solution**: Both methods provided are efficient, but ensure that the solution is applied correctly with a time complexity of O(n) and space complexity of O(1) for XOR method.
- **Additional Notes**:
Performance: Both methods are efficient with time complexity O(n) and space complexity O(1) for the XOR method. The set method has a space complexity of O(n).
- **Use Cases**: Useful for problems involving unique identification among duplicates, such as inventory management, data deduplication, and more.
## The Minion Game
**Definition**: The Minion Game is a game involving two players, Kevin and Stuart, who compete to score points by creating substrings from a given string. Kevin scores points with substrings starting with vowels, while Stuart scores with substrings starting with consonants. The player with the highest score wins.

- **Problem Statement**
Given a string S, calculate the scores for both players:

Kevin scores by counting substrings that start with a vowel.
Stuart scores by counting substrings that start with a consonant.
Determine the winner based on the scores.

- **Example**:
Input: "BANANA"
- **Output**:
Kevin's Score: 9 (Substrings starting with vowels: A, A, A, AN, ANA, ANAN, ANANA, ANA, ANANA)
Stuart's Score: 12 (Substrings starting with consonants: B, BAN, BANA, BANAN, BANANA, N, NA, NAN, NANA, AN, ANAN, ANANA)
Result: Stuart 12 Kevin 9 Stuart
- **Solution**:
    - **Algorithm**:

    - Initialize Scores: Start with scores of 0 for both players.
    - Iterate through String: For each character in the string, determine if it is a vowel or a consonant.
    - Calculate Scores:
        - For each vowel at position i, there are len(S) - i substrings starting with that vowel.
        - For each consonant at position i, there are len(S) - i substrings starting with that consonant.
    - Compare Scores: Print the player with the highest score, or if scores are tied, print "Draw".
    - **Python Code**:
    ```python
    def minion_game(S):
        vowels = "AEIOU"
        kevin_score = 0
        stuart_score = 0
        length = len(S)
        
        for i in range(length):
            if S[i] in vowels:
                kevin_score += length - i
            else:
                stuart_score += length - i
        
        if kevin_score > stuart_score:
            print("Kevin", kevin_score)
        elif stuart_score > kevin_score:
            print("Stuart", stuart_score)
        else:
            print("Draw")

        ```
    - Example:
    ```python
        minion_game("BANANA")
        ```
- **Common Problems**:
    - **Problem**: Incorrect score calculation due to not accounting for all possible substrings.

        - **Solution**: Ensure that for each character, you correctly count the number of substrings starting from that character to the end of the string.
    - **Problem**: Handling large strings efficiently.

        - **Solution**: The algorithm runs in O(n) time complexity, which is efficient for large strings.
- **Additional Notes**:
Performance: The solution provided runs in linear time, O(n), where n is the length of the string. This is optimal for this type of problem.
- **Use Cases**: Useful for understanding substring operations, game scoring algorithms, and performance optimization in competitive programming.

## Triangle Quest
## Triangle Quest 2

## Tuples
**Definition**: A tuple is an immutable sequence type in Python, used to store a collection of items. Unlike lists, tuples cannot be modified after creation, making them useful for fixed data collections.

- **Syntax**:
    - Creating a Tuple:

    ```python
    my_tuple = (1, 2, 3, 4)
    ```
    - Creating a Tuple with One Item:

    ```python
    single_item_tuple = (1,)  # Note the comma
    ```
    - Creating an Empty Tuple:

    ```python
    empty_tuple = ()
    ```
- **Example**:s
    - Basic Tuple:

    ```python
    my_tuple = (1, 2, 3, 4)
    print(my_tuple)  # Output: (1, 2, 3, 4)
    ```
    - Accessing Elements:

    ```python
    my_tuple = (1, 2, 3, 4)
    print(my_tuple[0])  # Output: 1
    ```
    - Slicing Tuples:

    ```python
    my_tuple = (1, 2, 3, 4, 5)
    print(my_tuple[1:4])  # Output: (2, 3, 4)
    ```
    - Nested Tuples:

    ```python
    nested_tuple = (1, (2, 3), 4)
    print(nested_tuple[1])  # Output: (2, 3)
    ```
    - Tuple Unpacking:

    ```python
    my_tuple = (1, 2, 3)
    a, b, c = my_tuple
    print(a, b, c)  # Output: 1 2 3
    ```
    - Concatenating Tuples:

    ```python
    tuple1 = (1, 2, 3)
    tuple2 = (4, 5, 6)
    combined_tuple = tuple1 + tuple2
    print(combined_tuple)  # Output: (1, 2, 3, 4, 5, 6)
    ```
    - Repeating Tuples:

    ```python
    my_tuple = (1, 2, 3)
    repeated_tuple = my_tuple * 3
    print(repeated_tuple)  # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)
    ```
- **Common Operations**:
    - Length of a Tuple:

    ```python
    my_tuple = (1, 2, 3, 4)
    length = len(my_tuple)
    print(length)  # Output: 4
    ```
    - Check Membership:

    ```python
    my_tuple = (1, 2, 3, 4)
    print(2 in my_tuple)  # Output: True
    ```
    - Index of an Element:

    ```python
    my_tuple = (1, 2, 3, 4)
    index = my_tuple.index(3)
    print(index)  # Output: 2
    ```
    - Count of an Element:

    ```python
    my_tuple = (1, 2, 3, 2, 2)
    count = my_tuple.count(2)
    print(count)  # Output: 3
    ```
- **Common Problems**:
    - **Problem**: Trying to modify elements of a tuple.

        - **Solution**: Remember that tuples are immutable. To modify a tuple, create a new tuple with the desired changes.
    - **Problem**: Incorrectly creating a single-item tuple (missing comma).

        - **Solution**: Always include a comma when creating a single-item tuple.
- **Additional Notes**:
Immutability: Tuples are immutable, meaning once they are created, their elements cannot be changed, added, or removed.
- **Use Cases**: Tuples are often used for fixed collections of items, such as function return values, or in situations where immutability is required.
## What's Your Name
**Definition**: The "What's Your Name" problem is a simple exercise in string manipulation where you need to format a string that consists of a person's first and last names, and then print a greeting using these names.

- **Problem Statement**
You are given two strings: the first name and the last name. Your task is to format and print a greeting that includes both names.

- **Input**:

Two strings: firstName and lastName
- **Output**:

A formatted greeting: "Hello {firstName} {lastName}! You just delved into python."
- **Example**:
    - **Input**:

    ```python
    firstName = "John"
    lastName = "Doe"
    ```
    - **Output**:

    ```python
    Hello John Doe! You just delved into python.
    ```
- **Solution**:
    - **Algorithm**:

        - Read Input: Read the input strings for first name and last name.
        - Format Greeting: Use string formatting to create the greeting message.
        - Print Greeting: Output the formatted greeting.
    - **Python Code**:
    ```python
    def print_greeting(first_name, last_name):
        greeting = f"Hello {first_name} {last_name}! You just delved into python."
        print(greeting)

    ``` 
    - Example:
    ```python
    first_name = "John"
    last_name = "Doe"
    print_greeting(first_name, last_name)
    ```
- **Common Problems**:
    - **Problem**: Incorrect string formatting.

        - **Solution**: Ensure you use the correct string formatting method. In Python, f-strings or str.format() can be used to insert variables into strings.
    - **Problem**: Input is not handled correctly.

        - **Solution**: Make sure that input strings are read and handled correctly before formatting them into the output.
- **Additional Notes**:
Performance: This problem is straightforward and performs in constant time O(1), as it involves simple string operations.
- **Use Cases**: Useful for practicing basic string manipulation and formatting in Python.
## Write a function
**Definition**: The "Write a Function" problem involves implementing a function to determine if a given string is a valid identifier according to specific rules. This problem typically tests your understanding of string manipulation and validation in Python.

- **Problem Statement**
You need to write a function to determine if a given string is a valid identifier. According to the problem's rules, the string should be:

A non-empty string.
Contain only alphabetic characters and underscores (_).
Start with an alphabetic character or an underscore, but not a digit.
- **Input**:

A single string: s
- **Output**:

True if the string is a valid identifier.
False otherwise.
- **Example**:
- **Input**:

```python
s = "var_name"
```
- **Output**:

```python
True
```
- **Input**:

```python
s = "1var_name"
```
- **Output**:

```python
False
```
- **Solution**:
    - **Algorithm**:

        - Check if the string is non-empty.
        - Verify that the first character is not a digit.
        - Ensure all characters in the string are either alphabetic or underscores.
    - **Python Code**:
    ```python
    def is_valid_identifier(s):
        if not s:
            return False
        if not s[0].isalpha() and s[0] != '_':
            return False
        return all(c.isalpha() or c == '_' for c in s)
    ``` 
- Example:
    ```python
    print(is_valid_identifier("var_name"))  # Output: True
    print(is_valid_identifier("1var_name")) # Output: False
    ```
- **Common Problems**:
    - **Problem**: Handling empty strings or strings that start with digits.

        - **Solution**: Check if the string is empty and if the first character is a valid starting character (alphabet or underscore).
    - **Problem**: Strings containing invalid characters.

        - **Solution**: Ensure that all characters in the string are either alphabetic or underscores.
- **Additional Notes**:
Performance: This solution is efficient with time complexity O(n), where n is the length of the string, due to the need to check each character.
- **Use Cases**: Useful for validating identifiers in programming languages, variable names, or other scenarios where specific naming conventions are required.
