#remove 20 in this list.
list1 = [5, 20, 15, 20, 25, 50, 20]
i=0
a=[]
c=0
while i <len(list1):
    if list1[i]==20:
        c+=1
    else:
        a.append(list1[i])
    i+=1
print(a)