# Monthly salary Calculation
basic_salary = 30000
hra=0.20 * basic_salary
da=0.10 * basic_salary
deepavali_bonus=5000

employee_gross_salary = basic_salary + hra + da + deepavali_bonus
print(employee_gross_salary)

#Tax deduction
tax=0.10 * employee_gross_salary
print(tax)
employee_net_slary =employee_gross_salary - tax
print(employee_net_slary)
