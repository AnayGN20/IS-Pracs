

key = input("Enter Key : ")

def encrypt(key):
    plain_text = input("Enter Plain text : ")
    key = key
    # plain_text = "GEEKSFORGEEKS"
    key_final=''
    while len(key) < len(plain_text):
        key += key
    if len(key)-len(plain_text) > 0:
        key_final = key[:-(len(key)-len(plain_text))]
        print(key_final)
    else:
        key_final = key
    

    A_INDEX = ord('A')
    cipher_text = []
    for i in range(len(plain_text)):
        p_index = ord(plain_text[i]) - A_INDEX
        k_index = ord(key_final[i]) - A_INDEX

        e_index = (p_index+k_index)%26 
        cipher_text.append(chr(e_index+A_INDEX))

    cipher_text = "".join(cipher_text)
    return cipher_text

def decrypt(key):
    cipher_text = input("Enter cipher text : ")
    
    while len(key) < len(cipher_text):
        key += key

    if len(key)-len(cipher_text) > 0:
        key_final = key[:-(len(key)-len(cipher_text))]
        print(key_final)
    else:
        key_final = key

    A_INDEX = ord('A')
    plain_text = []
    for i in range(len(cipher_text)):
        c_index = ord(cipher_text[i]) - A_INDEX
        k_index = ord(key_final[i]) - A_INDEX

        e_index = (c_index-k_index)%26 
        plain_text.append(chr(e_index+A_INDEX))

    plain_text = "".join(plain_text)
    return plain_text
    
print("---CHOOSE MODE---")
print("[1] ENCRYPT")
print("[2] DECRYPT")
mode = int(input("Enter Number : "))

if mode==1:
    print("CIPHER : ",encrypt(key))
elif mode==2:
    print("PLAIN : ",decrypt(key))
else:
    print("Invalid Number")