# age = int(input("What is your age?:"))

# if age >= 9:
#     height = int(input("What is your height? (in cm)"))
#     if height > 130:
#         print("You are good to go on the ride!!")
#     else:
#         print("Sorry, you are too short for the ride")
# else:
#     print("Sorry, you are too young to go on the ride.")


#     #Errors: line 6, greater than equals
#     # line 8 else if
#     # line 8 comparing to a string
#     #  line 11 not indented
# print("Your down payment is: ${}" .format(age))


IDEAL_CREDIT_SCORE = 720

uesrScore = int(input("Please enter your credit score: "))
housePrice = int(input("Please enter the price of your house: "))

if uesrScore >= IDEAL_CREDIT_SCORE:
    downpayment = 0.1 * housePrice
elif uesrScore < IDEAL_CREDIT_SCORE and uesrScore > 600:
    downpayment = 0.2 * housePrice
else:
    downpayment = 0.3 * housePrice

print("Your downpayment is ${}" .format(downpayment))
