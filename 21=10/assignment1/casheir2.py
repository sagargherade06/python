def calculate_note(amount):
    notes_count={}
    notes_count[10]=amount//10
    amount%=10
    notes_count[5]=amount//5
    amount%=5
    return notes_count
amount=int(input("enter the value cash withdrawn"))
notes_count=calculate_note(amount)
print(f"{notes_count[10]},{notes_count[5]}")