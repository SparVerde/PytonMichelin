list_a=[1,2,3,4]
list_b=[4,5,6,7,8,17]
result_list=[]

if len(list_a)> len(list_b):
    short_list = list_b
    long_list = list_a
else:
    short_list = list_a
    long_list = list_b

for i in range(len(short_list)):
    result_list.append(list_a[i]+list_b[i])
#print(result_list)
slice_of_list_a= long_list[len(short_list):]
#print(slice_of_list_a)
result_list+=slice_of_list_a
print(result_list)
#Version 2 - Extend:
result_list.extend(slice_of_list_a) # another option to add the slice list
print(result_list)