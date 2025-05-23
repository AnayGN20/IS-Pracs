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

def encrypt(msg:None, e, n):
    if(msg==None):
        msg = input("Enter Message to Encrypt : ")

    print("Entered Encrypt")
    list_ascii = lambda x:ord(x)
    ascii_ans = map(list_ascii, msg)

    msg_list = list(ascii_ans)
    # print(msg_list)

    crypt = []
    for ascii in msg_list:
        c = (ascii ** e)%n
        crypt.append(chr(c))
    
    # print(crypt)
    return "".join(crypt);
    
def decrypt(crypt:None, d, n):
    if(crypt==None):
        crypt = input("Enter Envrypted Message : ")
    plain = []
    for c in crypt:
        m = (ord(c) ** d) % n
        plain.append(chr(m))

    return "".join(plain);

def rsa_start(msg:str, mode:str, p, q):
    
    n = p*q

    phi_n = (p-1)*(q-1)
    # print(phi_n)

    e = calculate_e(phi_n);
    # print(e)

    d = calculate_d(phi_n, e)
    # print(d)

    public_key = (e,n);
    private_key = (d,n);

    # print("Public key : ", public_key)
    # print("Private key : ", private_key)

    if(mode=='encrypt'):
        encrypted_text = encrypt(msg, e, n);
        return encrypted_text
    else:
        decrypted_text = decrypt(msg, d, n);
        return decrypted_text;

def do_vernam(key, text):
    
    key_final=''
    while len(key) < len(text):
        key += key
    
    key_final = key[:-(len(key)-len(text))] if len(key)!=len(text) else key
 
    A_index = ord('A') #Done to bring alphabets on scale of 0 to 25
    cipher_text = ""
    for i in range(len(text)):
        p_index = ord(text[i])-A_index
        k_index = ord(key_final[i])-A_index

        e_index = p_index ^ k_index
        e_index = e_index%26
        cipher_text += chr(e_index+A_index)

    return cipher_text
    

print("VERNAM CIPHER")
print("-------------\n")
key_main = input("Enter Key : ").strip().upper()
message = input("Enter Message : ").strip().upper()

cipher_text = do_vernam(key_main, message)
print(cipher_text)


print("RSA ENCRYPTION")
print("-------------\n")
p = int(input("Enter Prime Number 1 : "))
q = int(input("Enter Prime Number 2 : "))

encrypted_text = rsa_start(cipher_text, "encrypt", p, q)
print(encrypted_text)

print("RSA DECRYPTION")
print("-------------\n")
decrypted_text = rsa_start(encrypted_text, "decrypt", p, q)
print(decrypted_text)


print("VERNAM DECIPHER")
print("-------------\n")

print("MESSAGE = ", do_vernam(text=decrypted_text, key=key_main))





