def find_quardinate(x,y):
    if x>0 and y>0:
        return "first_quadrant" 
    elif x<0 and y>0:
        return "second_quadrant" 
    elif x<0 and y<0:
        return "third_quadrant"
    elif x>0 and y<0:
        return "fourth_quadrant" 
    else:
        if x==0 and y==0:
            return"origin"
        elif x==0:
            return"y axis"
        elif y==0:
            return"x axis"
x=int(input("enter the x coordinate"))
y=int(input("enter the y coordinate"))
style=find_quardinate(5,10)
print(f"your coordinate point is({x},{y})")
print(f"your qudrant{style}")

