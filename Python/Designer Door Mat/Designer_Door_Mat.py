# Enter your code here. Read input from STDIN. Print output to STDOUT
# Input dimensions
n, m = map(int, input().split())
# Generate the top half of the pattern
for i in range(1, n, 2): 
    pattern = (".|." * i).center(m, '-')
    print(pattern)

# Print the middle "WELCOME" line
print("WELCOME".center(m, '-'))

# Generate the bottom half of the pattern
for i in range(n-2, 0, -2): 
    pattern = (".|." * i).center(m, '-')
    print(pattern)
