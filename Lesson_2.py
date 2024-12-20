# Average of prime numbers from m to n
def ktnt(n):
    i=2
    while (i*i<=n) and (n%i!=0):
        i+=1
    return (i*i>n) and (n>1)
m = 10
n = 20
tong=0
dem=0
for i in range(m,n+1):
    if ktnt(i):
        tong+=i
        dem+=1
if dem>0:
    tbc=tong/dem
    print('%0.2f'%tbc)
else:
    print('-')