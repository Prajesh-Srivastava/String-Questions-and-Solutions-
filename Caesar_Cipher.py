def caesar(n,s,k):
    p=''
    for i in s:
        if ord(i)>=97 and ord(i)<=122:
            w=ord(i)
            
            for j in range(k):
                if w==122:
                    w=97
                else:
                    w+=1
            p=p+chr(w)
        elif ord(i)>=65 and ord(i)<=90:
            w=ord(i)
            
            for j in range(k):
                if w==90:
                    w=65
                else:
                    w+=1
            p=p+chr(w)
        else:
            p+=i
            continue
    return(p)

n=int(input())
s=input()
k=int(input())
e=caesar(n,s,k)
print(e)
