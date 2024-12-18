num=int(input("enter a number"))
num_str=str(num)
reversed_str=num_str[::-1]
if reversed_str==num_str:
    print("palindrome number")
else:
    print("is not palindrome number")