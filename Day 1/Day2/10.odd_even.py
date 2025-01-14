l = [1,2,33,4,56,77,8,9,11,12]   
odd =[]
even = []
print("a = ", l,"\nodd = ",odd,"\neve = ",even)
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
#print(l)
print("Odds:\n",odd)
print("Evens:\n",even)
