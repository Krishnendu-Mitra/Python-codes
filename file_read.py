#code by krish
src = input("Enter file name: ")
fp=open(src,'r')
for each_line in fp:
  print(each_line)
fp.close()
