def is_perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    return sum==n
for n in range(1,100):
    if is_perfect(n):
        print(n)