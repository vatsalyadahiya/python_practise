#12. Print pattern: 
#1 
#12 
#123 
#1234 
#12345

num = 0
i = 1
while i <= 5:
    num = num * 10 + i
    i+=1
    print(num)