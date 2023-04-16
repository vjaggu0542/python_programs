str1= "qwerwertyuuioasddfgfghhjkjklzxcxxcccvbnbnm"
result = ""

for i in str1:
    count = 0
    for j in str1:
        if i == j:
            count = count + 1
        if count > 1:
                break
    if count == 1:
                result = result + i
print(result)

