#Create a program to find the largest number in list using for loop...

lst = [100,11,33,44,22,179098,55,99,9,1,1200]
lst = ['1','100','11','33','44','22','199979098','55','99','9','1','1200']
for i in range(len(lst)-1):
    if lst[i]>lst[i+1]:
        temp = lst[i]
        lst[i] = lst[i+1]
        lst[i+1] = temp
print(lst[i+1])
    