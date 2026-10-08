#20.Pyramid Pattern 
#Print: 
    #* 
   #*** 
   #***** 
   #******* 
   #********* 

for i in range(1,10,2):
    print("  ",end="")
    for j in range(1,i+1):
        print("*",end="")
    print()