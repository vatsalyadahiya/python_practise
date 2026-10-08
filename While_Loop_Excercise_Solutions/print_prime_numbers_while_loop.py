#18. Print prime numbers between 1 to 50 using while loop.
n = 2 

while n <= 50:
    i = 2
    while i < n:
        if n % i == 0:
            break
        i += 1
    else:
        print(n)

    n += 1 