#List Demo
#use 13>Given list Element
A = [1, 2, 3, 27, 56, 99, 0, 78, 18]
print(A, "type of A:",type(A))
A[0] = 98 #value change in index 0 by 98
print(A)
A = [42, "krish", False, 9.8, 0] #multi datatype in a list
print(A)
print(A[2:4]) #slicing list print
A[1] = 38
print(A[0:-1]) #negative indexing


#use 14> list casting
A = [1, 8, 5, 2, 7, 8, 21, 38, 71, 15, 99]
print(A)
A.sort() 
print(A) #sorted list print
A.reverse()
print(A) #reverse list print
A.append(4)
print(A) #insert a new value
A.insert(8,545)
print(A)
A.pop(5) #pop the 5th index's element
print(A)
A.remove(38) #remove the given value
print(A,"\n")


#use 17>Simple user given List element
m1 = int(input("Enter marks number 1: "))
m2 = int(input("Enter marks number 2: "))
m3 = int(input("Enter marks number 3: "))
m4 = int(input("Enter marks number 4: "))
m5 = int(input("Enter marks number 5: "))
m6 = int(input("Enter marks number 6: "))
m7 = int(input("Enter marks number 7: "))
m8 = int(input("Enter marks number 8: "))
myList = [m1, m2, m3, m4, m5, m6, m7, m8] #insert all element in a list
print(myList,"\ntype is: ",type(myList))
myList.sort()
print(myList)


#User given list by for loop
myList = [] #empty list
for i in range(1,9,1):
    b = int(input(f"Enter marks number {i}: "))
    myList.append(b) #insert the user given value
print(myList)


#User given list by function calling
def data():
    myList = []
    for i in range(1,9,1):
        b = int(input(f"Enter marks number {i}: "))
        myList.append(b)
    display(myList)
def display(myList):
    print(myList)
#main function
data()


#use 18>sum of list
A = [2, 4, 56, 7]
print(A[0]+A[1]+A[2]+A[3])
print(sum(A)) #shortcut way
print(sum(A[1:3])) #smart way[0:]


#Type casting(tuple to list)
T = (5,10,15,20,25,30,35,40)
print(T," type is",type(T))
L = list(T)
print(L," type is",type(L))
