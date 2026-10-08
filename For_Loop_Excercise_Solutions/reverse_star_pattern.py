#Q17. Reverse Star Pattern 
#Print: 
#***** 
#**** 
#*** 
#** 
#*

for i in range(1,6):
    for j in range(1,7-i):
        print("*",end='')
    print()