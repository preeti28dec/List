
list1= [23, 14, 56, 12, 19, 9, 15, 25, 31, 42, 43] 
i=0
even=0
odd=0
sum_even=0
sum_odd=0
while i<len(list1):
    if list1[i]%2==0:
        even+=1
        sum_even+=list1[i]
    else:
        odd+=1
        sum_odd+=list1[i]
    i+=1
print("that is all count of lenght =",i)
print("that is sum of all number",sum_even+sum_odd)
print("its a average of all number is sum",sum_even+sum_odd/i)
print("its a count of even",even)
print("its a count of odd",odd)
print("its a average of even",sum_even/even)
print("its a average of odd",sum_odd/odd)
print("its sum of even number",sum_even)
print("its sum of odd number",odd)