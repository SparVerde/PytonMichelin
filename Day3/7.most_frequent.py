import pprint
numbers = [101,202,303,202]
frequencies = {}

for no in numbers:
    if no in frequencies:
        frequencies[no] = frequencies[no] + 1
    else:
        frequencies[no] =  1
print("Version 1: ",frequencies)
#pprint.pprint(frequencies)
# define first 0 value for frequeny[no] in two loops 
#for no in numbers:
    #frequencies[no] = 0

#Version 2 - the most performant one
numbers = [101,202,303,202]
frequencies = {}

for no in numbers:
    frequencies[no] = frequencies.get(no, 0)+ 1
print("Version 2: ",frequencies)

#Version 3
numbers = [101,202,303,202]
frequencies = {}

for no in numbers:
    frequencies[no] = numbers.count(no)
print("Version 3: ",frequencies)

#Continue with Version 2 - the most performant one
#Initial array
numbers = [101,303,202,303,202,200,200,404,404]
#Dictionnary of frequencies
frequencies = {}

#Iterate trough array
for no in numbers:
    #check if it is even
    if no % 2 == 0:
        #get existing value 0 and add 1 to i
        frequencies[no] = frequencies.get(no, 0)+ 1

print("Version 2b: ",frequencies)
# count frequencies:
#fins maximum frequency value (int)
max_freq = 0
for i in frequencies:
    if frequencies[i] > max_freq:
        max_freq = frequencies[i]
print('Maximum freq', max_freq)

#build a collection of frequincies
#Find the numbers that have the highest frequency
max_frequencies = []
for f in frequencies:
    if frequencies[f] == max_freq:
        max_frequencies.append(f)

print(max_frequencies)


max_frequencies.sort()
print(max_frequencies[0])
# or in one line:
print(min(max_frequencies))