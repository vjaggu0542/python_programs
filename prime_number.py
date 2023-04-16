num = 5
a=0
if(num==0):
      print(" 0 is not prime")
elif(1<num):     
 for x in range(2,num):
        if num % x == 0:
             a += 1
             break
 if a==1 :
      print(num , " is not prime")
 else:
      print(num , " is prime")     
            
    
        
    