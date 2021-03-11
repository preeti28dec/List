number = 30
n = [10, 11, 12, 13, 14, 17, 18, 19] 
i=0
c=[]
while i< len(n):
    j=0
    a=[]
    while j<i:
        if n[i]+n[j]==number:
            a.append(n[i])
            a.append(n[j])
            c.append(a)
        j=j+1
    i=i+1
print(c)