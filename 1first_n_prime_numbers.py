num = 20
for n in range(3,num):
    for i in range(2,n):
        if n%i ==0:
           break
    else:
          print(n)
