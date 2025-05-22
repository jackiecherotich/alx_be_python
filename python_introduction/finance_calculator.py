# finance_calulator.py

#Prompt user for the input variables


monthly_income = float(input("Enter your monthly income: ")) #Prompt their monthly income
monthly_expenses = float(input("Enter your total monthly expenses: ")) 


# Calculate Monthly Savings:
monthly_savings = monthly_income - monthly_expenses


#Project Annual savings
interest = 0.05
projected_savings = (monthly_savings * 12 + (monthly_savings * 12 * interest))

#Output results
print ("Your monthly savings are $" ,monthly_savings,)
print ("Projected savings after one year, with " , interest, "is: $ " ,projected_savings)
