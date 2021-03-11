i=1
a=[]
while i<=10:
    user=int(input("enter the number"))
    a.append(user)
    i+=1
print(a)
i=-1
n=[]
while i>=-len(a):
    n.append(a[i])
    i-=1
print(n)

