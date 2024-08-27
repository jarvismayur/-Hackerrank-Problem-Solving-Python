# Enter your code here. Read input from STDIN. Print output to STDOUT
num_of_elements = int(input())
elements = list(map(int, input().split()))

unique_elements = set()
duplicate_elements = set()

for num in elements:
    if num in unique_elements:
        duplicate_elements.add(num)
    else:
        unique_elements.add(num)

# Find the unique element by subtracting duplicates
result = unique_elements.difference(duplicate_elements)
print(result.pop())  # Since only one unique element is left, we can directly pop it