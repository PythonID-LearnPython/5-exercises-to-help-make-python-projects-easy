n= 20
a=[-10,40,20,-15,10]
demduong=0
demam=0
c=[]
b=[]
for i in range(len(a)):
    if a[i]<0:
        demam+=1
        c.append(a[i])
    if a[i]>0:
        demduong+=1
        b.append(a[i])
print(demduong,demam)
if demduong==0:
    print('-')
if demam==0:
    print('-')
for i in range(len(b)):
    print('%0.0f'%b[i],end=' ')
print()
for j in range(len(c)):
    print('%0.0f'%c[j],end=' ')