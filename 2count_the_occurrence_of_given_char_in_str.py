str1="zsdfsfvavvvvvvvvvvvvffsfcccvvv"
cha ="v"

#method1
#print(str1.count(cha))

#method2
count = 0
for i in range(len(str1)):
    if (str1[i] == cha):
        count += 1
print(count)