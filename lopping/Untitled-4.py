def find_perfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    return sum==num
num=int(input("enter a number"))
if find_perfect(num):
    print("is perfect number",num)
else:
    print("is not perfect number",num)