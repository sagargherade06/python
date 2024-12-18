def calculate_notes(amount):
    notes = [10, 5, 1]
    note_count = {10: 0, 5: 0, 1: 0}
    
    for note in notes:
        note_count[note] = amount // note  # Calculate how many of this note
        amount %= note  # Update amount to the remainder after using these notes
    
    return note_count

amount = int(input("Enter the amount: "))
note_count = calculate_notes(amount)

print("Number of notes:")
print("10s:", note_count[10])
print("5s:", note_count[5])
print("1s:", note_count[1])
