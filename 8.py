rc=int(input())
l=eval(input())
s=0
for i in range(rc):
    s+=l[i][i]
print(s/rc)