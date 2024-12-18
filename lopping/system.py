known=['sagar','manisha','pramav','pranita']
while True:
    print("*""*",117)
    print("\n hi!my name is tarvis")
    name=str(input("what is your name"))
    if name in known:
      print("helow{}!".format(name))
      remove=input("would you like to be removed frome the system ?(y/n)").strip().lower()
      if remove=="y":
         known.append(name)
      elif remove=="n":
         print("no problem,I did't want to leave anyway:")
    else:
       print("hummm i don't think i have meet you yet{}".format(name))
       add=input("would you like to be removed frome the system ?(y/n)").strip().lower()
       if add=='y':
          known.append(name)
       elif add=='n':
          print("no warries see around")        
         