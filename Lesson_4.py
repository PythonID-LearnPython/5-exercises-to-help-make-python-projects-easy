# Greatest common divisor
a = 20
b = 6
while a!=b:
    if a>b:
        a=a-b
    else:
        b=b-a
print(a)