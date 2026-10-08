#7. Find factorial of a number entered by user.
n = int(input("Enter a number to find its factorial: "))
fact = 1
a = 1

while a <= n:
    fact = fact * a
    a += 1

print("The factorial is:", fact)