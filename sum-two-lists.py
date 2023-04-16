from unittest import result


l1=[1,2,3]
l2=[4,5,6]
print("original list")
print(l1)
print(l2)
result=map(lambda x,y:x+y,l1,l2)
print("result")
print(list(result))
