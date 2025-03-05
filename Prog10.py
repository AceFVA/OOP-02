# Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

num1 = int(input("Num1: "))
num2 = int(input("Num2: "))

if num1 < num2:
    num1 += 1
    step = 1
else:
    num1 -= 1
    step = -1

for i in range(num1, num2, step):
    print(i) 
