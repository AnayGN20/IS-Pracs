plain_text= input("Enter Plain Text : ").upper()
key = int(input("Enter Key : "))
list_temp = list(plain_text)
A_index = ord('A')

encrypt = lambda x:(chr(A_index+((ord(x)+3-A_index)%26)))
cypher = map(encrypt, list_temp)
print("Cipher Text : ", end='')
for text in cypher:
    print(text, end='')

