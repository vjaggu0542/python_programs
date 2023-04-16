n="A2B5C7"
a=len(n)
b=[]
c=[]
for i in range(a):
    if n[i].isnumeric():
        b.append(int(n[i]))
    else:
        c.append(n[i])
for k,s in enumerate(c):
    print(s*b[k])
