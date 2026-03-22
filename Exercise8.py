#Write the program count the number of vowels स्वर (जैसे अँग्रेज़ी में a, e, i, o, u) in string 

count = 0
name = "bhushan satish jain"
name_split = name.split()
print(name_split)
for i in range(len(name)):
    if name[i] == 'a' or name[i] == 'e' or name[i] == 'i' or name[i] == 'o' or name[i] == 'u':
        count = count + 1
print(count)


'''
name = "bhushansatishjain"
vowels = "aeiou"
count = 0

for ch in name:
    if ch in vowels:
        count += 1

print(count)

'''
'''
name = "bhushansatishjain"
vowels = "aeiou"
word_count = {}
for word in name:
    if word in vowels:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] =  1
print(word_count) 
'''