def show(n):
    if n == 0:
        return 1
    else:
        result = n + show(n - 1)
        print(result)  # Print the intermediate result
        return result

show(5)
print(show(5))
