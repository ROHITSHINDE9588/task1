subject1 = float(input("Enter marks for Subject 1: "))
subject2 = float(input("Enter marks for Subject 2: "))
subject3 = float(input("Enter marks for Subject 3: "))

passing_marks = 40

if subject1 >= passing_marks and subject2 >= passing_marks and subject3 >= passing_marks:
    print("You have passed in all subjects.")
else:
    print("You have not passed in all subjects.")
