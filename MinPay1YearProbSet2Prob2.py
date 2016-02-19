monthlylowPayment = 10
monthlyhighPay = balance
monthlyInterestRate = annualInterestRate /12
newBal = balance

while newBal > 0:
    monthlyPayment += 10
    newBal = balance
    month = 0

    while month < 12 and newBal > 0:
        newBal -= monthlyPayment
        interest = monthlyInterestRate * newBal
        newBal += interest
        month += 1
print " Lowest Payment:", monthlyPayment