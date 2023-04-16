str1 = "123456addsdsd"
result = 0

for i in str1:
    if i.isdigit():
        result = result + int(i)
print(result)
