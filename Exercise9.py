#write a program to reverse the words in a sentace(not the letters)


name = "Python is very easy to learn"#= "bhushan satish jain"
print(name)
name_split = name.split()
print(name_split)
reversed_words = name_split[::-1]
result = " ".join(reversed_words)
print(result)
'''

sentence = "Python is very easy to learn"

words = sentence.split()        # split sentence into words
reversed_words = words[::-1]    # reverse the list of words
result = " ".join(reversed_words)
print(result)
'''

