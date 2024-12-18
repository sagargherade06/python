def calculate_note(amount):
    notes=[10,5,1]
    notes_count={10:0,5:0,1:0}
    for note in notes:
        notes_count[note]=amount//note
        amount%=note
    return notes_count
amount=int(input("enter the value withdrawn"))
notes_count=calculate_note(amount)
print(f"10:{notes_count[10]}")
print(f"5:{notes_count[5]}")
print(f"1:{notes_count[1]}")