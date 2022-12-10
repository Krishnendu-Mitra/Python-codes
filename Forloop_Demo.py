#for loops

#simple for loop
n = 5
for i in range(n):
    print(i)

#user define for loop
n = int(input("Enter the last number: "))
for i in range (n):
    print(i)

#function base for loop
def fun1(n):
    for i in range(n):
        i = i + 2
    i = i / 2
    return i
def fun2(n):
    for i in range(n):
        i = n - 1
    i = i * n
    return i
#main
n = int(input("Enter the a number: "))
a = fun1(n)
b = fun2(n)
print("Your answer is = ",a+b)