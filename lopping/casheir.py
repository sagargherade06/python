def calculate_note(amount):
    note_10=amount//10
    amount%=10
    note_5=amount//5
    amount%=5
    note_1=amount
    return note_10,note_5,note_1
amount=int(input("enter the amount"))
note_10,note_5,note_1=calculate_note(amount)
print('10s',note_10)
print('5s',note_5)
print('1s',note_1)
