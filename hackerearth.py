N=int(input('enter length of string'))
S=input('enter first string')
T=input('enter second string')
t=T
for i in range(len(T)):
    T=t
    if T == S :
        print(i)
        break
    else:
        t=T[-1]
        for j in range(N-1):
            t+=T[j]
            continue
