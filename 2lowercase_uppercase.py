str1 = "abcdef"
res = ""
for i in str1:
    if i.islower():
        i = i.upper()
    res = res + i
print(res)
