Weight = int(input("Enter Weight "))
unit = input("(L)bs or (K)gs: ")
if unit.upper() == "L":
    converted = Weight / 0.45
    print("Weight in Lbs : ", converted)
else:
    converted = Weight * 0.45
    print("Weight in Kgs : ",converted)

######################################### With String Formatting ##########################################
weight = int(input("Weight:  "))
unit = input("(L)bs or (K)gs: ")
if unit.upper() == "L":
    Converted = weight*0.45
    print(f"You are {Converted} Kilos ")
else:
    Converted = weight/0.45
    print(f"You are {Converted} Lbs ")