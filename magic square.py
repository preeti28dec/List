# that is magic square 
m_s = [[8, 3, 4],[1, 5, 9],[6, 7, 2]] 
i=0
r1,r2,r3=0,0,0
c1,c2,c3=0,0,0
d1,d2=0,0
while i<len(m_s):
    r1=r1+m_s[0][i]
    r2=r2+m_s[1][i]
    r3=r3+m_s[2][i]
    c1=c1+m_s[i][0]
    c2=c2+m_s[i][1]
    c3=c3+m_s[i][2]
    d1=d1+m_s[i][i]
    d2=d2+m_s[1][-i-1]
    i+=1
if r1==r2==r3==c1==c2==c3==d1==d2:
    print("that is magic square hai ")
else:
    print("that is not a magic square")