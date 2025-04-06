n = int(input("Enter 1st prime number : "))
g = int(input("Enter 2nd Prime Number : "))

from random import randrange

x = randrange(1, 10);
print("X for Alice : ",x)
y = randrange(1, 10);
print("Y for Bob : ",y)

A = (g**x) % n;
print("A : ",A)
B = (g**y) %  n ;
print("B : ",B)
while(True):
    k1 = (B**x) % n;
    k2 = (A**y) % n;
    if k1==k2:
        print("Shared Key : ",k1);
        break;
    else:
        A = k1;
        B = k2;

