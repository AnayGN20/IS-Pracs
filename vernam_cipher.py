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

        e_index = ~(p_index ^ k_index)
        e_index = e_index%26
        cipher_text += chr(e_index+A_index)

    return cipher_text
    

print("VERNAM CIPHER")
print("-------------\n")
key = input("Enter Key : ").strip().upper()
message = input("Enter Message : ").strip().upper()

print(do_vernam(key, message))
