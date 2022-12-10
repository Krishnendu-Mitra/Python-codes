#code by krish
txt = input("Enter your data: ")

#process 1
p1 = txt
p1 = p1.replace("A"," ")
p1 = p1.replace("E"," ")
p1 = p1.replace("I"," ")
p1 = p1.replace("O"," ")
p1 = p1.replace("U"," ")

p1 = p1.replace("a"," ")
p1 = p1.replace("e"," ")
p1 = p1.replace("i"," ")
p1 = p1.replace("o"," ")
p1 = p1.replace("u"," ")

print("Vowel less data = \n",p1)

#process 2
p2 = txt