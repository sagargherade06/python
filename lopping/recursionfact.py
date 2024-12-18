def fact_no(n):
    if n==0:
        return 1
    fact=n*fact_no(n-1)
    return fact
fact_no(5)
print(fact_no(5))