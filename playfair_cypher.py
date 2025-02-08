def create_key_matrix(key_final):
    alphabet_counter = 0;
    A_index = ord('A')
    key_matrix = []
    for i in range(ROWS):
        for j in range(COLUMNS):
            if key_final:
                key_matrix.append(key_final[0])
                key_final.remove(key_final[0])
            else:
                while True:
                    current_chr = chr(A_index + alphabet_counter)
                    if current_chr=='J' or current_chr in key_matrix:
                        alphabet_counter+=1
                    else:
                        key_matrix.append(current_chr)
                        break
            # print(alphabet_counter)
    return key_matrix




def to_diagraphs(text):
    last_char = ''
    temp = []
    esc = 'X'

    for i in text:
        if i == last_char:
            temp.append(esc)
            temp.append(i)            
        else:
            temp.append(i)
            last_char = i

    if(len(temp)%2 == 1):
        temp.append('Z')
    
    pairing = lambda l: [l[i:i+2] for i in range(0, len(l), 2)]
    diagraphs = pairing(temp)

    return diagraphs


def encrypt(key_matrix_final, plain_text_diagraphs):
    cipher_text_list = []

    for i in plain_text_diagraphs:
        for row in key_matrix_final:
            if row.count(i[0])==1:
                row0 = key_matrix_final.index(row)
                column0 = row.index(i[0])
            if row.count(i[1])==1:
                row1 = key_matrix_final.index(row)
                column1 = row.index(i[1])

        if row0 == row1:
            cipher_text_list.append(key_matrix_final[row0][(column0+1)%COLUMNS])
            cipher_text_list.append(key_matrix_final[row1][(column1+1)%COLUMNS])
        
        elif column0 == column1:
            cipher_text_list.append(key_matrix_final[(row0+1)%ROWS][column0])
            cipher_text_list.append(key_matrix_final[(row1+1)%ROWS][column1])

        else:
            cipher_text_list.append(key_matrix_final[row0][column1])
            cipher_text_list.append(key_matrix_final[row1][column0])

    return cipher_text_list


key = input("Enter key : ").strip().upper()

key = key.replace(' ', '')
while key.isalpha() is False:
    print("!!! KEY CAN ONLY CONTAIN ALPHABETS !!!")
    key = input("Enter key : ").strip().upper()

while key.__contains__('I') and key.__contains__('J'):
    print("!!! KEY CANNOT CONTAIN I AND J TOGETHER !!!")
    key = input("Enter key : ").strip().upper()

key = list(key)
key_final = []

for i in key:
    if i == 'J':
        i = 'I'
    if key_final.count(i)>0:
        continue
    else:
        if key.count('J')>0:
            key
        key_final.append(i)
    
ROWS = 5
COLUMNS = 5

key_matrix = create_key_matrix(key_final)
to_matrix = lambda l, n : [l[i:i+n] for i in range(0, len(l), n)]
key_matrix_final = to_matrix(key_matrix, ROWS)




print("\n---KEY MATRIX---\n[",)
for i in key_matrix_final:
    print("   ",i)
print("]\n")


plain_text = input("Enter Plain Text : ").strip().upper()
plain_text = plain_text.replace('J', 'I')
plain_text = plain_text.replace(' ','')

while plain_text.isalpha() is False:
    print("!!! KEY CAN ONLY CONTAIN ALPHABETS !!!")
    plain_text = input("Enter key : ").strip().upper()



plain_text_diagraphs = to_diagraphs(plain_text)

print("Plain Text : ",plain_text)
cipher_text_list = encrypt(key_matrix_final, plain_text_diagraphs)
cipher_text = "".join(cipher_text_list)
print("Cipher Text : ",cipher_text)


