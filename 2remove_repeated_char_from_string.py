str1="abcdaaabbbbcccdlkdhakjdhaskdhsajdkajkaskjdhdjkjdjahakjhdkdjkdqwertyuioplkjhgfdsazxcvbnm"
result = ""
for i in str1:
    if i not in result:
        result = result + i
    else:
        pass

  

print(result)
      