import random

numbers = []
for i in range(10):
    numbers.append(random.randint(1, 100))

print("List:", numbers)

max_number = numbers[0]
min_number = numbers[0]

for number in numbers:
    if max_number < number:
        max_number = number
    if min_number > number:
        min_number = number

print(f"Max: {max_number}")
print(f"Min: {min_number}")