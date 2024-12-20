# Find x in the array or not, if yes print "Yes" and print the position, otherwise write "No"
n = 20
x = 10
a= [10,40,11,17,86]
dem=0
vt=0
for i in range(len(a)):
    if x==a[i]:
        dem+=1
        vt=i
        break
if dem==0:
    print('No')
else:
    print('Yes')
    print(vt)