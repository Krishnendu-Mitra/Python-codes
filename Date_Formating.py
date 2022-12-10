#date formateing
n = input("Enter the date(dd/mm/yyyy): ")
d = int(n[0:2])
m = int(n[3:5])
y = int(n[6:])
if((d<=31 and d>=1) and (m<=12 and m>=1) and (y<=5000 and y>=0) and (n[2] == "/" and n[5] == "/")):
    print(" Date =",d,"\n","Month =",m,"\n","Year =",y)
    n = n.replace("/","-")
    print("New formate =",n)
else:
    print("Error your date system act like vitale information!")
#happy ending