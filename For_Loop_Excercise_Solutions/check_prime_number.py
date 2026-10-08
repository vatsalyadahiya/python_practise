#Q15. Prime Number Check 
#Take a number from the user and check whether it is prime using for-else.
 
number = int(input("Enter number: "))

if number == 2:
    print("Prime number")
else:
    for i in range(2, number):
        if number % i == 0:
            print("Not prime")
            break
    else:
        print("Prime number")