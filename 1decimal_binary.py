n=16
l=[]
while n!=0:
  r = n%2
  l.append(r)
  n=n//2
l.reverse()

for i in l:
  print(i,end="")