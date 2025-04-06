key = "HACK"
plain_text = "REPEATATTACKTONIGHT"

plain_list = []
temp_list = []

key_dict = {k: key.index(k) + 1 for k in key}
# print(key_dict)

for p in plain_text:
    temp_list.append(p)
    if len(temp_list) == len(key):
        plain_list.append(temp_list)
        temp_list = []
if temp_list:
    plain_list.append(temp_list)

#print(plain_list)
while True:
    if len(plain_list[-1]) != len(key):
        plain_list[-1].append('Z')
    else:
        break


key_dict_sorted = dict(sorted(key_dict.items()))
cipher_text = []
temp_list = []
index_list = list(key_dict_sorted.values())

for i in range(len(key)):
    index = index_list[i]
    for j in range(len(plain_list)):
        temp_list.append(plain_list[j][index-1])
    cipher_text.append(temp_list)
    temp_list = []
 
print(key_dict_sorted)

plain_text = []
index_list = list(key_dict_sorted.values())
print(index_list)
for i in range(len(key)):
    for j in range(len(index_list)):
        if index_list[j] == i+1:
            index = j
            # print(index)

    temp_list.append(cipher_text[index])

plain_list = []
for i in range(len(temp_list[0])):
    for j in range(len(key)):
        plain_list.append(temp_list[j][i])

i=0
while True:
    i -= 1
    if plain_list[i] == "Z":
        plain_list.pop()
    else:
        break



print(cipher_text)

print("".join(plain_list))
    






