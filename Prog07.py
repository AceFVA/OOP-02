# Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

num_10 = input("Input 10 numbers separated by space: ")
list = num_10.split()
even = 0

for i in range(0,10):
    if int(list[i]) % 2 == 0:
        even = even + 1
        
print(even)
