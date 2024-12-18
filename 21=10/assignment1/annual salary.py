def calculate_tax(annual_salary): 
    if annual_salary<0:
        print("not valid basic salary")
        return 
    if annual_salary<=250000:
        income_tax=0
    elif annual_salary<=500000:
        income_tax=(500000-250000)*0.10
    elif annual_salary>500000:
        income_tax=(250000)*0.10+(annual_salary-500000)*0.20
    return income_tax
annual_salary=int(input("enter the annual salary"))
income_tax=calculate_tax(annual_salary)
print('your annual basic salary is',income_tax)
