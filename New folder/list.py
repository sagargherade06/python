numbers=input("enter a list numbers):")# get the input frome user
numbers=[int(x) for x in numbers.split()]#create the list store the input value
#find greates numbers
greatest=max(numbers)
#coun the number in how many times is occur
count=numbers.count(greatest)
print(count)
print(greatest)