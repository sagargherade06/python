num=int(input("enter a number"))
num_str=str(num)#conver integer to string
length=len(num_str)#calculat the string length
#sum function is use
print(length)
sagar=sum(int(digit)**length for digit in num_str)
if sagar==num:
    print(f"your number is{num}armstrong")
else:
    print(f"you number is{num} is not armstrong")