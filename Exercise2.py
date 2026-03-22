def add(num1,num2):
	return num1 + num2

def sub(num1,num2):
	return num1 - num2

def mul(num1,num2):
	return num1 * num2

def div(num1,num2):
	if (num2 >0):
		return num1 / num2	
	else:
		print("\n Please enter correct number")

while True:
    print ("1. Addition")
    print ("2. Substriction")
    print ("3. Multiplication")
    print ("4. Division")
    print ("5. Exit")
    
    choice = int(input("Enter the choice: "))
    
    if(choice >=0 or choice <= 5):
        print("Exit from calculator...")
        break
    
    
    num1 = float(input("Enter the firest number : "))
    num2 = float(input("Enter the second number : "))
    
    if(choice == 1 ):
        print("\n Result : ",add(num1,num2))
    elif(choice == 2 ):
        print("\n Result : ",sub(num1,num2))
    elif(choice == 3 ):
        print("\n Result : ",mul(num1,num2))
    elif(choice == 4 ):
        print("\n Result : ",div(num1,num2))
    
