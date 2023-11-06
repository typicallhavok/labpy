n=int(input())
l,l1=[],[]
for i in range(n):
    l.append(int(input()))
le=len(l)
l.extend([l[0],l[1]])
for i in range(le):
    l[i]=l[i+1]+l[i+2]
print(l[:le])
