print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

per_person_total = (bill / people) * (tip / 100 + 1)
final_amount = "{:.2f}".format(per_person_total)
print(f"Each person should pay: ${final_amount}")
