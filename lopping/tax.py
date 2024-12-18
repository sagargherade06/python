def calculate_income_tax(anual_salary):
    if anual_salary<250000:
        incometax=0
    elif anual_salary<=500000:
        incometax=((anual_salary-2500000)*0.10)
    else:
        incometax=((2500000*0.10)+(anual_salary-500000)*0.20)
        return incometax
anual_salary=float(input("enter anual salary"))
incometax=calculate_income_tax(anual_salary)
print("your anual salary is",anual_salary)
print("your tax is",incometax)    