Report Card                                                                                                                                                          marks = [[78, 76, 94, 86, 88],[91, 71, 98, 65, 76],[95, 45, 78, 52, 49]]
i=0
sum1=0
while i<len(marks):
    j=0
    while j<len(marks[i]):
        sum1=sum1+marks[i][j]
        j=j+1
    print(sum1)
    i=i+1