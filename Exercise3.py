number = int(input("Enter a non-negative integer: "))
fact = 1
i = 2
while(i <= number):
    fact *=  i
    i = i + 1
    
print(f"The factorial of {number} is {fact}.") 


'''
number = int(input("Enter a non-negative integer: "))
fact = 1
for i in range(1,number+1):
    fact *=  i
print(f"The factorial of {number} is {fact}.") 
'''
