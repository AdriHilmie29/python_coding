# A bank is charging 6% interest per year for a loan. Monthly payments will be made for a certain period of time. Calculate the monthly payment amount a person needs to pay by
# asking the user to enter the loan amount and time period.



interestRate = 1.06

initialLoan = input('Enter initial loan: RM')
initialLoan = int(initialLoan)
timePeriod = input('Enter time period (in months):')
timePeriod = int(timePeriod)
print(' ')

print('Interest rate: 6%')
monthlyPayment = initialLoan*interestRate/timePeriod
print('Monthly payment =', monthlyPayment)
print(' ')

input('Press ENTER to exit')
