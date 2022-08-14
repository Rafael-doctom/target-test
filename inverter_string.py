# This program reverses string characters

# Getting string from user
string_to_reverse = input('Type in a string that you want to reverse: ')

# Setting up variables
reversed_string_list = []
string_item_index = len(string_to_reverse) - 1

# Getting reversed string on a list
for i in range(len(string_to_reverse)):
    reversed_string_list.append(string_to_reverse[string_item_index])
    string_item_index -= 1

# Converting reversed list to reversed string
reversed_string = ''.join([str(item) for item in reversed_string_list])

# Printing final result
print(reversed_string)
