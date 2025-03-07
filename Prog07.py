# Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

num_10 = input("Enter 10 numbers (space-separated): ")
num = num_10.split()
even = 0

for i in range(10):
    if int(num[i]) % 2 == 0:
        even += 1

print(even)
