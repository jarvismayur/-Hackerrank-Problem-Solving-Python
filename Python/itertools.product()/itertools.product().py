# Taking input as a string using input function  
input_str = input()  
  
# Converting input string to a list of integers  
A = input_str.split()  
A = [int(num) for num in A]  
# Taking input as a string using input function  
input_str = input()  
  
# Converting input string to a list of integers  
B = input_str.split()  
B = [int(num) for num in B]  

from itertools import product
print(" ".join(str(tup) for tup in list(product(A, B))))
