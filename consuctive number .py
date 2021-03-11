that is consuctive number                                                                                               n=int(input("enter how many list elements"))
a=[]
i=1
while i<=n:
    x=int(input("enter the no"))
    a.append(x)
    i+=1

print(a)
j=0
count=0
while j < len(a)-1:
    if a[j+1]-a[j]!=1:
        print("false")
        break
    else:
        count+=1
    j+=1
if count==len(a)-1:
    print("true")