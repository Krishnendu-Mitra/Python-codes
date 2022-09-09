n = int(input("Enter the number = "))
a = list(str(n))
b = a[0::1]
r = a[-1::-1]
if b == r:
    print("Yes, it is palindrom number")
else:
    print("No, it is not palindrom number")