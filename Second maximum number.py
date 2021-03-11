#that is maximum and seced maximum number in list 
num = [50, 40, 23, 70, 56,69, 12, 5, 10, 7] 
max=0
sec=0
i=0
a=len(num)
while i<a:
	if num[i]>max:
		max=num[i]
	i=i+1
	j=0
	while j<i:
		if sec<num[j]< max:
			sec=num[j]
		j+=1
print(sec)

