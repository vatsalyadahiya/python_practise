#15. Keep taking input numbers until user enters 0, then print total sum.
number = int(input("Enter number: "))
a = 0
while number!=0:
      a+=number
      number = int(input("Enter number: "))
 
print("Total sum is",a)