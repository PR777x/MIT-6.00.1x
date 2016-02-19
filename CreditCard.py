balance = 4213
annualInterestRate = .2
monthlyPaymentRate = .04
month = 1 
unPaidBal = balance


while month <= 12:
    minPay = monthlyPaymentRate * balance
    
    print 'Month: ' + str(month)
    month += 1
    
    print 'Minimum monthly payment: ' + str(minPay)
    unPaidBal -= minPay
    interest = monthlyPaymentRate * unPaidBal
    unPaidBal += interest
    
    print 'Remaining balance: ' + str(unPaidBal)
    balance = unPaidBal
    