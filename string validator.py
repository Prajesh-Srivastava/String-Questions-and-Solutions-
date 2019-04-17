s=input()
a=s
print(a.isalnum())
c=len(a)
for i in range(c):
    if ord(a[i])>= 65 and ord(a[i])<=90 or ord(a[i])>= 97 and ord(a[i])<= 122:
        print('True')
        break
    else:
        continue
else:
    print('False')

for i in a:
    if ord(i)>= 48 and ord(i)<= 57:
        print('True')
        break
    else:
        continue
else:
    print('False')
for i in a:
    if  ord(i)>= 97 and ord(i)<= 122 :
           print("True")
           break
    else:
        continue
else:
    print('False')
for i in a:
    if  ord(i)>= 65 and ord(i)<= 90 :
           print("True")
           break
    else:
        continue
else:
    print('False')

