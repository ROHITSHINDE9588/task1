basic_salary = float(input("Enter Basic Salary: "))

hra = 0.20 * basic_salary   
da = 0.10 * basic_salary   
ta = 0.05 * basic_salary    

pf = 0.12 * basic_salary   
tax = 0.08 * basic_salary   

gross_salary = basic_salary + hra + da + ta
net_salary = gross_salary - (pf + tax)

print("\n--- Employee Salary Slip ---")
print("Basic Salary:", basic_salary)
print("HRA (20%):", hra)
print("DA (10%):", da)
print("TA (5%):", ta)
print("Gross Salary:", gross_salary)
print("PF (12%):", pf)
print("Tax (8%):", tax)
print("Net Salary:", net_salary)
