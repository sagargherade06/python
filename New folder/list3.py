#start with empty dictionary
marks_dict={}
# get the marks frome the user
for i in range(3):
    subject=input(f"enter subject{i+1}")
    marks=input(f"enter the marks{subject}")
    marks_dict[subject]=int(marks)
    print("marks dictionary",marks_dict)