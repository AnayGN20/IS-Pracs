def gcd(a, b):
    while b!=0:
        a, b = b, a%b;
    return a

def calculate_e(phi_n):
    for e in range(2, phi_n):
        if gcd(e, phi_n)==1:
            return e

def calculate_d(phi_n, e):
    #phi_n = phi_n+1;
    i=1;
    while(True):
        phi_2 = phi_n*i + 1;
        if phi_2%e == 0:
            return int(phi_2/e);
        i+=1;

def encrypt(msg:None):
    if(msg==None):
        msg = input("Enter Message to Encrypt : ")

    list_ascii = lambda x:ord(x)
    ascii_ans = map(list_ascii, msg)

    msg_list = list(ascii_ans)
    print(msg_list)

    crypt = []
    for ascii in msg_list:
        c = (ascii ** e)%n
        crypt.append(chr(c))
    
    print(crypt)
    return "".join(crypt);
    
def decrypt(crypt:None):
    if(crypt==None):
        crypt = input("Enter Envrypted Message : ")
    plain = []
    for c in crypt:
        m = (ord(c) ** d) % n
        plain.append(chr(m))
    return "".join(plain)

p = int(input("Enter Prime Number 1 : "))
q = int(input("Enter Prime Number 2 : "))

n = p*q

phi_n = (p-1)*(q-1)
print(phi_n)

e = calculate_e(phi_n);
print(e)

d = calculate_d(phi_n, e)
print(d)

public_key = (e,n);
private_key = (d,n);

print("Public key : ", public_key)
print("Private key : ", private_key)

# print(encrypt("TPSPTPXBUMSX"))
print(decrypt(encrypt("TPSPTPXBUMSX")))

