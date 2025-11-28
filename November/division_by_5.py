numbers_list = [21, 25, 30, 35, 12, 13, 5]

result = ""
for number in numbers_list:
    if number % 5 == 0:
        result += str(number) + " "

print(result)

