numbers=(1,2,3,5,6,7,8,9)
for value in range(5,100,5):
  while value%2==0:
    print("the even no",value)
    break
  else:
    print("the odd no",value)

