def do_vignere(key, text, mode):
    text_len = len(message)
    key_final=''

    
    while len(key) < text_len:  #Appends key till the length of plain_text
        key += key 

    
    key_final = key[:-(len(key)-text_len)] if len(key)!=text_len else key #Removes the extra letters of key so that key and plain text length are same

    A_INDEX = ord('A')
    crypt_text = ""
    
    for i in range(text_len):
        p_index = ord(text[i]) - A_INDEX
        k_index = ord(key_final[i]) - A_INDEX

        e_index = (p_index+k_index)%26 if mode==1 else (p_index-k_index)%26 #Main Logic for encryption and decryption

        crypt_text += chr(e_index+A_INDEX)

    return crypt_text
    

print("---CHOOSE MODE---")
print("[1] ENCRYPT")
print("[2] DECRYPT")
mode = int(input("Enter Number : "))
if mode!=1 and mode!=2:
    print("Wrong Mode\n")
message = input("Enter Message : ").strip().upper()
key = input("Enter Key : ").strip().upper()

print(do_vignere(key, message, mode))
