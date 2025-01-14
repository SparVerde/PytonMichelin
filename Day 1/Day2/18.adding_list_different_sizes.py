list_a=[1,2,3,4,5,6,7,8]
list_b=[4,5,6,7,8]
result_list=[]
for i in range(len(list_b)):
    result_list.append(list_a[i]+list_b[i])
#print(result_list)
slice_of_list_a= list_a[len(list_b):]
#print(slice_of_list_a)
result_list+=slice_of_list_a
print(result_list)
#Version 2 - Extend:
result_list.extend(slice_of_list_a) # another option to add the slice list
print(result_list)