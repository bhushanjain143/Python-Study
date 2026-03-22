#Write a program to reverse a list and remove the duplicate using a set 
'''

lst = [100,11,33,44,22,179098,55,99,9,1,1,1200,11]

lst = ['1','100','11','33','44','22','bhus','55','99','9','1','1200']
rev = lst[::-1]
print(rev)
new_tetx = set(rev)
print(new_tetx)
'''
a = [100,11,33,44,22,179098,55,99,9,1,1,1200,11]

a = ['1','100','11','33','44','22','bhus','55','99','9','1','1200']
i, j = 0, len(a) - 1

while i < j:
    a[i], a[j] = a[j], a[i]
    i += 1
    j -= 1

print(a)