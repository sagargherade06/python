def prime_no(n):
    for i in range(2,(int(n**0.5)+1)):
        if n%i==0:
            return False
    return True
primenumber=[num for num in range(1,100) if prime_no(num)]
print(primenumber)
