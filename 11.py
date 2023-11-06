n=int(input())
di={}
s=''
for i in range(n):
    x=eval(input())
    di[x]=type(x)
    if type(x) is str:
        s+=x+' '
print(s.strip())