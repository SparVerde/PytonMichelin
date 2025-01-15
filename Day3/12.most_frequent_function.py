def most_frequent_value(numbers): #numbers are the parameter
    #Check if list is empty
    if not numbers:
        return-1
    #Dictionary of frequencies
    #using dict comprehension
    frequencies_dict = {
       no : numbers.count(no) for no in numbers if no %2 == 0
    }
    return frequencies_dict

    # we have other functions:
def most_frequent_value_2(numbers): #numbers are the parameter
 
    frequencies_dict = {
       no : numbers.count(no) for no in numbers if no %2 == 0
    }
    max_freq = max(frequencies_dict.values())
    if max_freq < 2:
        return -1
    
    max_frequencies_array = [f for f in frequencies_dict if frequencies_dict[f] == max_freq]
    return min(max_frequencies_array)

print(most_frequent_value([101,202,303,404,200,202,200,200,200,400,400,400,400,400,404]))
print(most_frequent_value_2([101,202,303,404,200,202,200,200,200,400,400,400,400,400,404]))
print(most_frequent_value([]))