print("Welcome to the calculator.")
bill=float(input("What was the total bill? $"))
tip=int(input("What percentage tip would you like to give? 10, 12, or 15? "))
split=int(input("How many people to split the bill? "))
total=(bill/split)*(1+tip/100)
print(f"Each person should pay: ${round(total,2)}")