#l=[20,30,40]
#print(max(l))

#method 2
num1=float(input("please enter a number: "))
num2=float(input("please enter a number: "))
num3=float(input("please enter a number: "))

if (num1>=num2) and (num2>=num3):
    largest=num1
elif (num2>=num3) and (num2>=num1):
    largest=num2
else:
    largest=num3
print("largest number is :",largest)
