user_number = int(input("N: "))

if user_number < 0:
    print("Factorial cannot be found for negative numbers!")

else:
    if user_number == 0:
        print("0! = 1")
    
    else:
        result = 1
        factors = [] 
        
        for i in range(1, user_number + 1):
            result *= i
            factors.append(str(i)) 
        factr_string = " x ".join(factors)

        print(f"{user_number}! = {factr_string} = {result}")
