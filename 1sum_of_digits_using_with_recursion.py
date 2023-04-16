def sum_dig(n):
    if n<10:
        return n
    else:
        return n%10 + sum_dig(n//10)

number = 6
print("sum of digits ",sum_dig(number))