'''
a = "Hello"
b= "World"
#print(a+ " "+b)
#print(f"{a} {b}")

text = "Python Programming"
print(text)
print(text[0:7])        # print firest 6 character from the string
print(text[-6:])#(6:-1) # print last 6 character from the string
print(text[::2])#(6:-1) # print every second character from the string

#reverse the sting using slicing

text = "Python Programming"
print(text[::-1])

Str = " i love python programming "
#remove extra spaces from both endswith
print(Str.strip())
#convert it to title case
print(Str.title())
#Count how many times "o" appears
print(Str.count("0"))
# Check if the string "123abc" is alphanumeric
print(Str.isalnum())

#Using format(),create a sentance: "My name is john and I am 25 year old" by passing JOHN and 25 variable 
do the same using f-string
    
name = "John"
age = 25
print(f"My name is {name} and I am {age} year old")

#string manipulation
#1. given sentance = 'Coding in python is fun', replace "fun" with "awesome" and print it.

sentance = "Coding in python is fun"
new = sentance.replace("fun","awesome")
print(new)
#2. find the index of the word "python" in sentance.
print(sentance.find("python"))
#3. Convert the entire sentance to uppercase and print it.
print(sentance.upper())
'''
#count the vowels in sentance
sentance = "Coding in python is fun"
vowels = "aeiou"
count = 0 
for i in sentance.lower():
    #print(sentance[i])
    if sentance[i] in vowels:
        count = count + 1
print(count)

#==========
#Check the string is palindrome or not
ustring = "Bhushan"
newstring = ustring[::-1]
if ustring == newstring:
    print("string is palindrome")
else:
    print("string is not palindrome")