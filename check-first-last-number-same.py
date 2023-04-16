list1 = [10,20,30,40,50,60,70,10]

def checkvalues(str1):
    frist=str1[0]
    last=str1[-1]
    if frist==last:
        print("true")
    else:
        print("false")
checkvalues(list1)