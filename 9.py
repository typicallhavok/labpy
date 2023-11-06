rc=int(input())
l=eval(input())
l2=[]
l1=[]
for i in range(rc):
    l1=[]
    for j in range(rc):
        l1.append(l[j][i])
    l2.append(l1)
print(l2)