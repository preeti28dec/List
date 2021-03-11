#that is maximum number in list 
num = [50, 40, 23, 70, 56, 12, 5, 10, 7] 
max=0
i=0
a=len(num)
while i<a:
	if num[i]>max:
		max=num[i]
	i=i+1
print(max)