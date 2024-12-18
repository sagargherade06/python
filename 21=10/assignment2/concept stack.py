list=[]
while True:
    element=input("enter the value of list")
    if element.lower()=='finish':
        break
    if element in list:
        print("you allready inserted value")
    else:
        list.append(element)#push the element
print("push the element",list)
if list==0:
    print("no value")
peek=list[-1]
#peek the element
print(f"topest element is lis{peek}")
#peek the element
list.pop()
print("pop the list",list)# pop the elementd