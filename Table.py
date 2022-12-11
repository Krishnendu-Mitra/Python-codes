#code by krish
def limitTable(t):
    n = int(input("Enter the last limit: "))
    if(n >= 1):
        for i in range(1,n+1,1):
            print(t,"*",i,"=",t*i)
    else:
        print("Sorry user your given limit is not valid, try again")
        limitTable(t)
#---------------------
def valueTable(t):
    val = int(input("Enter the last value: "))
    if(val>=1):
        if(val % t == 0):
            i = 1
            while val == (t*i):
                print(t,"*",i,"=",t*i)
                i = i + 1
        else:
            print("User your given value is not excite in",t,"table so i give you near value\n")
            i = 1
            while (val <= t*i):
                print(t,"*",i,"=",t*i)
                i = i + 1
    else:
        print("Sorry user your given value is not valid, try again!")
        valueTable(t)
#---------------------
def choice(t):
    wise = int(input("what you want(Last limit=0 or last value=1): "))
    if(wise == 0):
        limitTable(t)
    elif(wise == 1):
        valueTable(t)
    else:
        print("Sorry user i am not understand your wise,\nPlease try again later!\n")
#main-----------------
t = int(input("Which table you want: "))
if(t >= 1):
    choice(t)
else:
    print("Sorry user your give table head is not valid for our universe!")
#happy ending