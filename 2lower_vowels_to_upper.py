str1 = "assdehfhihsohdsu"
vow = "aeiou"
res = ""
for i in str1:
  if i in vow:
        res = res + i.upper()
  else:
        res = res + i

print(res)
