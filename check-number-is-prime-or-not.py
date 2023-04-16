def primecheck(number):
    if number>1:
        for num in range(2,number):
            if number%num == 0:
                return "not aprime"
            else:
                return "prime"
print(primecheck(4))


        