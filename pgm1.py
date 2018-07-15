total = 0.0

while True:	
    number = input("Enter number here :")

    if number == '':
        break
    try:
        total = total + float(number)
    except ValueError: 
        continue
		
print("Total is", total)

