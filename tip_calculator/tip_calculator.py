#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
bill = input("What was the total bill? $")
# print(type(bill))
tip = input("How much tip would you like to give? 10, 12, or 15? ")
# print(type(tip))
people = input("How many people to split the bill? ")
# print(type(people))
bill = float(bill)
tip = float(tip)
people = int(people)

bill_with_tip = tip / 100 * bill + bill

each = round(bill * (tip/100 + 1) / people, 2)
each1 = "{:.2f}".format(bill_with_tip / people)
print(f"Each person should pay: ${each1}")
