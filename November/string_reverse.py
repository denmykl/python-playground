original_string = "Hello World!"
temp_list = []

for char in temp_list:
    temp_list.insert(0, char)

reversed_string = ""
for char in temp_list:
    reversed_string += char


print(reversed_string)