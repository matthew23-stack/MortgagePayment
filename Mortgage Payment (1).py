def monthly_payment_amount(A, R, M):
    P = R*A/(1-(1+R)**-M)
    return P
def main():
    amount_of_loan = int(input("Enter the amount of loan: "))
    interest_rate = float(input("Enter the interest rate as percentage: "))
    interest_rate = interest_rate/100
    simple_or_compount = str(input("Please choose: Simple or Compound Interest "))
    months = int(input("Enter the desired numbers of months: "))
    

    payment_amount_permonth = monthly_payment_amount(amount_of_loan,interest_rate,months)
    print("The monthly payement amount is: ",format(payment_amount_permonth, '.2f'))
main()
