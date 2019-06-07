s=input()
u=s.lower()
w=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in w:
    if i in u:
        continue
    else:
        print('not pangram')
        break
else:
    print('pangram')
