# Write your code here
annual_salary = input("Enter your annual salary: ")
portion_saved = input("enter your percent of your salary to save as a decimal: ")
monthly_salary_saved = input(int(annual_salary)/12 * float(portion_saved))
total_cost = input("Enter cost of home: ")
porion_down_payment = .25 * int(total_cost)

current_savings = 0

i = 1
while current_savings < porion_down_payment:
    current_savings += monthly_salary_saved
    investment_return = current_savings * (.04/12)
    current_savings += investment_return
    1 += 1
print("it will take you",i,"months to save for downpayment!" )
