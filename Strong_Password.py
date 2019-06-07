n=int(input())
a=input()
p="0123456789"
lower_case = "abcdefghijklmnopqrstuvwxyz"
upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
special_characters = "!@#$%^&*()-+"
c=0
d=0
e=0
f=0
r=0
if len(a)>=6:
    for i in a:
        if i in p:
            c+=1
        elif i in lower_case:
            d+=1
        elif i in upper_case:
            e+=1
        elif i in special_characters:
            f+=1
        else:
            r+=1
    if c==0:
        t=1
    else:
        t=0
    if d==0:
        q=1
    else:
        q=0
    if e==0:
        u=1
    else:
        u=0
    if f==0:
        y=1
    else:
        y=0
    m=t+q+u+y
    print(m)


else:
    w=6-len(a)
    print(w)


