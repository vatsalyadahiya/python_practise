# 10. Check whether a number is palindrome or not using while loop.
a = int(input("Enter the number: "))

temp = a
rev = 0

while temp > 0:
  digit = temp % 10
  rev = (rev * 10) + digit
  temp = temp // 10

if a == rev:
  print("Number is palindrome", a)
else:
  print("Number is not palindrome", a)