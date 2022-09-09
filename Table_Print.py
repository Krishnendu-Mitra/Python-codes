def check(T,N):
    if T>0 and N>0:
        table(T,N)
    elif T==0 or N==0:
        print("Syntex error!")
    else:
        print("Negative table is not valid in our universe!")
        return
def table(T,N):
    for i in range(1,N+1,1):
        print(f"{T} * {i} =",T*i)
#main function
t = int(input("Entere the table = "))
n = int(input("Enter the range of table = "))
check(t,n)