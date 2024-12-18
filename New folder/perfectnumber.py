def is_perfect(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    return sum==n
isperfect=[num for num in range(1,101) if is_perfect(num)]
print(isperfect)
