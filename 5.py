n=int(input())
l,l1=[],[]
for i in range(n):
    l.append(int(input()))
k=int(input())
for i in l:
    if l.count(i)==k:
        l1.append(i)
print(l1)