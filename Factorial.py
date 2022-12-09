#code by krish
n = int(input("Enter the number: "))
m = n - 1
for i in range(n,1,-1):
  n = n * m
  m = m - 1
print("Factorial is = ",n) 
