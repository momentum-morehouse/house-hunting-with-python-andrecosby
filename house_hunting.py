# Write your code here
annual_salary = input("Enter your annual salary: ")
portion_saved = input("enter your percent of your salary to save as a decimal: ")
monthly_salary_saved = input(int(annual_salary)/12 * float(portion_saved))
total_cost = input("Enter cost of home: ")
print(total_cost)
portion_down_payment = .25 * int(total_cost)
print(portion_down_payment)


# current_savings = 0

i = 1
while current_savings < portion_down_payment:
    current_savings += monthly_salary_saved
    investment_return = current_savings * (.04/12)
    current_savings += investment_return
    1 += 1
print("Number",i,"months to save for downpayment for house" )
