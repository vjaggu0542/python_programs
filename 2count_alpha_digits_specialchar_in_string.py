str1 = "dsadsd231232132%^%&$%@$@#$@$@$1q"
digit = ""
alpha = ""
specialchar = ""

for i in str1:
    if i.isdigit():
        digit = digit + i
    elif i.isalpha():
         alpha = alpha + i
    else:
        specialchar = specialchar + i
print("total digits : ", len(digit), " total alpha: ", len(alpha), "total specialchar: ",len(specialchar))
