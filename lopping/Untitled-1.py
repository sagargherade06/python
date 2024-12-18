def find_primeno(n):
    if n<=1:
        return False
    for i in range(2,n):
     if n%i==0:
         return False
    return True
num=int(input("enetr a number"))
if find_primeno(num):
    print("prime no",num)
else:
    print("not prime number",num)    



