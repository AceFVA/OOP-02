# Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.

for i in range(0,101):
    if not(str(i).endswith("0") or str(i).endswith("5")):
        print(i)

'''
Alternative
num = 0

while num < 100:
    if not(str(num).endswith("0") or str(num).endswith("5")):
        print(num)
        num += 1
    else:
        num += 1
'''
