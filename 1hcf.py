num1=77
num2=154
if num1>num2:
    minimum = num2
else:
    minimum = num1
for i in range(1,minimum+1):
    if (((num1%i)==0) and((num2%i)==0)):
        hcf = i
print("hcf = ", hcf)
        


