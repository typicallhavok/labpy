s=input()
s1=''
for i in s:
    if i=='z':
        s1+='a'
    elif i=='Z':
        s1+='A'
    elif i.isalpha():
        s1+=chr(ord(i)+1)
    else:
        s1+=i
print(s1)