n = [1,2,3,4,5,10]
output = []
for i in range(1,n[-1]+1):
    if i not in n:
        output.append(i)
print(output)