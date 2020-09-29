# Write your code here
annual_salary = input("salary: ")
print(annual_salary)
portion_saved = input("percent of salary as decimal: ")
monthly_salary_saved = input(int(annual_salary)/12 * float(portion_saved))
print(monthly_salary_saved)

total_cost = input("Enter cost of home: ")
print(total_cost)

portion_down_payment = .25 * int(total_cost)
print(portion_down_payment)


current_savings = 0

i = 0

while current_savings < portion_down_payment:
    current_savings += monthly_salary_saved
    investment_return = current_savings * (.04/12)
    current_savings += investment_return
    i += 1
print("Number",i,)

