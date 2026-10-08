#17. Check whether a number is Armstrong number.
num = int(input("Enter number: "))
add = 0
copy = num
print("Original Number :",num)
while num>0:
    rem = num%10
    add = add+rem**3
    num = num//10
print("Number After Add :",add)
if copy==add:
    print("Armstrong")
else:
    print("not Armstrong")