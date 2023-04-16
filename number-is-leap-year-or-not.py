def leapyear(value1):
    return (((value1%4==0) and (value1%100!=0)) or (value1%400==0))
value1=2024
if (leapyear(value1)):
    print("this is leap year")
else:
    print("this is not a leap year")