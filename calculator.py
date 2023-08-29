first = float(input("Enter First No. => ")) 
sec = float(input("Enter Second Number => "))  
opr = str(input("Enter Operation (+,-,*,/)=>")) 

if opr== "+":
    total = first+sec
elif opr== "-":
    total=first-sec 
elif opr=="*":
     total=first*sec
elif opr=="/":
     total=first/sec 

print(total)
        