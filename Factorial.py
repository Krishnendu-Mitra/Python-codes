#factorial
n = int(input("Enter the number: "))
#x' = (x-1)*(x-2)*(x-3)*......*1
m = n - 1
for i in range(m,1,-1):
    n = n * i
    i = i - 1
print("Factorial is: ",n)