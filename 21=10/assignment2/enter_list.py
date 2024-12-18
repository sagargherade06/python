'''list=[]
element=input("enter a element")
list.extend(element)
list.append(5)
print(list)'''
list=[]
while True:
    number=input("enter the element (or to finsh done)")
    if number=='done':
        break
    list.append(number)
print(list)