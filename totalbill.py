print("Welcome to the tip calculator!")
totalbill=float(input("What was the total bill? $"))

tip=int(input("How much tip would you like to give? 10,12 or 15"))

number_of_people=int(input("How many people to split the bill?"))

percentage=tip/100
total_amount=totalbill*percentage
per_person =total_amount/number_of_people
round_value=round(per_person,2)
print(f"Each person should pay ${round_value}")


