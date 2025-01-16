# If-else Statement
age = 13
if age >= 18:
    print("Eligible for driving licence")
else:
    print("Not eligible for driving licence")

# Single line if else / Ternary Operator
marks = 56
result = "Pass" if marks >= 30 else "Fail"
print("The marks is enough for", result)

# Elif Statement
rank = 4634
if rank <= 100:
    print("You get a god rank")
elif rank <= 200:
    print("You get a average rank")
elif rank <= 500:
    print("You get a bad rank")
else:
    print("You get a horrible rank")

# Nested if-else
amount = 310
Loan = True

if amount >= 500:
    if Loan:
        print("Repay the Loan faster")
    else:
        print("No need to repay")
else:
    if Loan:
        print("You have time to repay the loan")
    else:
        print("Increase the money")

# Match case Statement
booleanValue = 9

match booleanValue:
    case 0:
        print("The value is zero")
    case 1:
        print("The value is one")
    case 2 | 3 | 4 | 5:
        print("The value can only have 0 and 1")
    case _:
        print("It is not a valid binary value")
