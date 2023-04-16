def recursion(list):
    total=0
    for ele in list:
        if type(ele)==type([]):
            total = total+recursion(ele)
        else:
            total=total+ele
    return total
print(recursion([1,2,3,[4,5],[6,7]]))