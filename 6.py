n=int(input())
l,l1=[],[]
for i in range(n):
    l.append(int(input()))
k=int(input())
l1=list(set(l))
l1.sort()
if len(l1)<k:
    print(None)
else:
    print(l1[k])