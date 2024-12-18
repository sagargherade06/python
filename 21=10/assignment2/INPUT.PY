values=[int(input(f"enter 5 numbers{i+1}:"))for i in range(5)]
if len(values)!=len(set(values)):
    print("DUPLICATES")
else:
    print("ALL UNIQUE")