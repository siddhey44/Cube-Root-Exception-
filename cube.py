num=int(input("enter the number :"))
def cube_root(num) :
    #check the number positive or not 
    if(num<0):
        raise Exception("Number is negative ")
    return num**(1/3)
print(cube_root (num))
    
    