# Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

num_10 = input("Input 10 numbers separated by space: ")
list = num_10.split()
num1 = list[0]

for i in range(1,10):
    num1 = int(num1) - int(list[i])
    
print(num1)
