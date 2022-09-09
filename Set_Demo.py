'''
    python set is unordered collection with no duplicate elements
    python set can be declared in 2 different ways
    {} and using set() functions
'''

#basket={'apple','orange','pear','apple','guava'}
#print(basket)
#print('orange' in basket)

#set is mutable and slicing is not possible as there are no fixed index

#sampleWord='umbrella'
#print(set(sampleWord))

flowers={"sunflowers","roses","lavender","tulips","goldcrest","lotus"}
indian_Flowers={"hibiscus","lotus","pinwheelflower"}

indian_Flowers.add("marigold")
print(indian_Flowers)

#set difference
print(indian_Flowers.difference(flowers))

#Intersection Operator
print(indian_Flowers.intersection(flowers))

print(indian_Flowers.isdisjoint(flowers))

print(indian_Flowers.issuperset(flowers))
print(indian_Flowers.issubset(flowers))

#symmetric difference
print(flowers.symmetric_difference(indian_Flowers))

print(flowers.union(indian_Flowers))

flowers.update(indian_Flowers)
print(flowers)

flowers.discard("roses")
print(flowers)

print(flowers.pop())
print(flowers)

flowers.clear()

print(flowers)
x=set()
print(type(x))

#frozenset is same as set

fs=frozenset(["g","o","o","d"])
print(fs)
#fs.pop()
#print(fs)
