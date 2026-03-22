'''
choice = int(input("Enter the days from 1 to 7: "))
match (choice):
    case 1: 
        print("The day is sunday")
    case 2: 
        print("The day is Monday")      
    case 3: 
        print("The day is Tuesday")
    case 4: 
        print("The day is Wednesday")
    case 5: 
        print("The day is Thrusday")
    case 6: 
        print("The day is Friday")
    case 7: 
        print("The day is Saturday")

    case _:
        print("Invalide choice")
        
'''
'''
total = 0
for i in range(1,101):
    total = i + total
print(total)
'''
'''
*
**
***
****
for i in range(5):
    print("*" * i )
'''
'''
i = 0
while (i<10):
    print(i)
    i = + i +1
'''
'''
Password = "Bhushan"
Enter_password = input ("Enter the passwored: ")

if (Password == Enter_password):
    print("Password is correct")
else:
    print("Wrong Password, Try again and enter password")
---------------
'''
'''
#Reverse the number  123 --> 321
a = 123 
print(int(str(a)[::-1]))
==========

s = "123"

# Initialize an empty string to hold reversed result
rev = ""

# Loop through each character in original string
for ch in s:
  
    # Add current character to front of reversed string
    rev = ch + rev

print(rev)

'''

123
num = int(input("Enter a number: "))
reversed_num = 0

while num > 0:
    last_digit = num % 10
    print(last_digit)
    reversed_num = (reversed_num * 10) + last_digit
    print(reversed_num)
    num //= 10
    print(num)

print("Reversed number:", reversed_num)

