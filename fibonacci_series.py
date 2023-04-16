n=10
a=0
b=1
print("fibonacci series are : ")
for i in range(0,n):
    if i<=1:
       result = i
       print(result)
    else:
        result = a+b
        a = b
        b = result
        print(result)
