
# PROBLEM: there is no limit for the value of y. 
import math, PremadeTimer

@PremadeTimer.time_this
def calculation(n):
    n=n[0]
    maxX=0
    corresponding_D=0
    counter=0
    for D in range(1,n+1):
        for y in range(1,10000):
            # skip if D is square
            if math.sqrt(D).is_integer(): break
            
            x=math.sqrt(1+D*y**2)
            if x.is_integer():
                counter+=1
                print("%d^2 - %d*%d^2 = 1"%(x,D,y))
                if x>maxX:
                    maxX=x
                    corresponding_D=D
                break
    return maxX,corresponding_D,counter

print(calculation(1000))