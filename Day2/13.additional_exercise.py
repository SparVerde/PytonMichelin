#two list with 1,2,3 and 4,5,6 create a new list with 1+4,2+5,3+6
a=[1,2,3]
b=[4,5,6]
c=[]
for i in range(len(a)):
    #print(a[i], b[i])
    c.append(a[i]+ b[i])

print (c)