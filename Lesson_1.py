# Check if it is a perfect square number or not
import math
def ktcp(n):
    if n<0:
        return False
    x=int(math.sqrt(n))
    return (x*x==n)
n=50

if ktcp(n):
    print('Yes')
else:
    print('No')