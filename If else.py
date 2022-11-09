# If Else Condition

#Predefined Conditions

hot = True
cold = False

if hot:
    print("It's a hot day")
    print("Drink water")
elif cold:
    print("Wear warm clothes")
else:
    print("It is a lovely Day")



#Program to print downpayment of a 1M house with good credit buyer

good_credit = True
bad_credit = False
House = 10000000

if good_credit:
    down_payment = 0.1 * House
    print("Buyer has good credit.\nNeed to pay: $",down_payment)
else:
    down_payment = 0.2 * House
    print("Buyer has bad credit, \n Need to pay: $",down_payment)
