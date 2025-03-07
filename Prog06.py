# Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

num_10 = input("Input 10 numbers (space-separated): ")
num = num_10.split()
num1 = num[0]

for i in range(1,10):
    num1 = int(num1) - int(num[i])
    
print(num1)
