#Q11. Skip Letter 
#Print each character of the string "PYTHON". 
#Skip the letter "O".

string = "PYTHON"

for i in string:
    if i=="O":
        continue
    print(i)