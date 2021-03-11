#Average Kitna Hai sum of even and odd
list1 = [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
even=0
odd=0
while i<len(list1):
    if list1[i]%2==0:
        even+=1
    else:
        odd+=1
    i=i+1
print(even/len(list1))
print(odd/len(list1))