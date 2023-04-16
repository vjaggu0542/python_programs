num = 27
sum = 0
for i in range(1,(num//2)+1):
    reminder = num%i
    if reminder ==0:
        sum = sum + i
if sum == num:
    print("given number is perfect number")

else:
    print("given number is not perfect number")