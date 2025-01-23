print("Welcome to the tip calculator!\n")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
total_bill = (bill + (tip/100 * bill))/people
print(f"Each person should pay ${total_bill:.2f}")