num = 1600
if (((num%4 ==0) and (num%100 !=0 )) or (num%400==0)):
    print(num," is leap year")
else:
    print(num," is not leap year")
