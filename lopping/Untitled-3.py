def find_armstrongnumber(num):
    num_str=str(num)
    length=len(num_str)
    sum_ofdigit=sum(int(digit)**length for digit in num_str)
    return sum_ofdigit==num
num=int(input("enter a number"))
if find_armstrongnumber(num):
    print("armstrng number",num)
else:
    print("not armstrong number",num)


"""
    def find_armstongnumber(num):
    num_str=str(num)
    length=len(num_str)
    sum_ofdigit=sum(int(digit)**length for digit in num_str)
    return sum_ofdigit==num
num=int(input("enter a number"))
if find_armstongnumber(num):
    print("armstrong number",num)
    """

    
