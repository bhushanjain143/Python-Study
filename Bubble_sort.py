'''
Bubble sort compares adjacent elements:
if lst[j] > lst[j + 1]:
Time Complexity:
Best Case: O(n) if optimized with swap flag
Average Case: O(n²)
Worst Case: O(n²)
'''
lst = [11,22,434,768768,5,67,8,99,9,8,99,27,9999999]
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        #print(i, "    ", j)
        if lst[i]>lst[j]:
            print(lst[i] , "  ",lst[j])
            temp = lst[i]
            lst[i]= lst[j]
            lst[j] = temp
            print("Temp",lst[i] , "  ",lst[j])
print(lst)
