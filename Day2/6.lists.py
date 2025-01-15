#definition of list
collection=[1,2,3,4] #collection=[1,2,3,4] is OK
print(collection, type(collection))

for i in collection:
    print("i = ",i)

    #Indexing a value from a list
    print("Position 0:", collection[0])
    print("Position 3:", collection[3])
    print("Position -1:", collection[-1])
    print("Position -4:", collection[-4])
    #list: 0,1,2,3 or -4,-3,-2,-1; -1 is always the last one!!!!!

    ##counting values
    print("lens =", len(collection))
    #updating value
    collection[2]=333 #this will not work for tuple
    #a tuple is immutable
    print(collection)

    #collection = "hello"
    print(collection)

    #add at the end - can't append
    collection.append(678)
    print(collection)

    #erase the last element on the list
    collection.pop()
    print(collection)

    #insert at a specicfic index
    collection.insert(0,"blue")
    print(collection)

    #erase at a specicfic index
    collection.pop(0)
    print(collection)