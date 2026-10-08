#08. First Negative Number 
#Given a list of numbers, print the first negative number and stop the loop.

numbers = [-2, -1, 0, 1, 2, 3]

for num in numbers:
    if num < 0:
        print(num)
        break