def word_count_in_file(filename):
    try:
        with open(filename,"r") as file:
            lines= file.readlines()
            line_count = len(lines)
            word_count = sum( len(line.split()) for line in lines)
            print(f"No of lines {line_count}")
            print(f"No of word {word_count}")
    except FileNotFoundError:
        print(f"The file {filename} is not found")
        
word_count_in_file("sample.txt")

n = 5
fact = 1
for i in range(2,n+1):
    fact = fact * i
print(fact)

i = 2
n = 5
fact = 1

while(i<=n):
    fact = fact * i
    i = i + 1 
print(fact)