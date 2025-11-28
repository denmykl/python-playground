list_1 = [1,2,3,4,5,6,7,8,9,10]
list_2 = [11,12,13,14,15,16,17,18,19,20]

result_list = []

for number in list_1:
    if number % 2 != 0:
        result_list.append(number)
        
print(result_list)
for number2 in list_2:
    if number2 % 2 == 0:
        result_list.append(number2)

print(result_list)