numbers=[2,3,5,10,3,5]
new_list = []
for i in numbers:
    new_list.append(i+1)
print(new_list)

new_list=[i+1 for i in numbers if i % 3 == 0]
print(new_list)