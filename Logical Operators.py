# OR Operator
# Both Conditions satisfy requirements
high_income = True
good_credit = True

if high_income or good_credit :
    print("Can Apply for Loan")

# Any one condition satisfies requirement
high_income = True
good_credit = False

if high_income or good_credit :
    print("Can Apply for Loan")

# AND Operator
high_income = True
good_credit = True

if high_income and good_credit :  # Both conditions need to be true
    print("Can Apply for Loan")
else:
    print("Not eligible for Loan")

# Not Operator (Changes the boolean expression
good_credit = True
criminal_record = False
if high_income and not criminal_record : # used NOT here
    print("Can Apply for Loan")