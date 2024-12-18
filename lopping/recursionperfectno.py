def sum_of_divisors(n, i=1):
    # Base case: If i reaches n, stop recursion
    if i == n:
        return 0
    # If i is a divisor of n, add i to the sum
    if n % i == 0:
        return i + sum_of_divisors(n, i + 1)
    # If i is not a divisor, move to the next i
    return sum_of_divisors(n, i + 1)

def is_perfect(n):
    # If the sum of divisors equals the number, it's a perfect number
    return n == sum_of_divisors(n)

# Test the function
n = 6
if is_perfect(n):
    print(f"{n} is a perfect number")
else:
    print(f"{n} is not a perfect number")
