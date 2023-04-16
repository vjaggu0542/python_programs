str1 = "this is string"
#print(len(str1))
def lencal(string1):
    count=0
    for char in string1:
        count+=1
    return count
print(lencal(str1))        