def calculate_perfectno(num):
    sum=0
    for i in range(1,num):
     if num%i==0:
            sum+=i
     return sum==num
num=int(input("enetr a number"))
if calculate_perfectno(num):
    print("is perfect no",num)
else:
    print("is not perfect")
