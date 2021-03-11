How to find all pairs in an array of integers whose sum is equal to the given numbern = [10, 11, 12, 13, 14, 17, ] 
i=0
c=[]
while i<len(n):
    a=[]
    j=0
    while j<i:
        if n[i]+n[j]==30:
            a.append(n[i])
            a.append(n[j])
            c.append(a)
        j=j+1
    i=i+1
print(c)