marks1 = float(input("Enter marks for Subject 1: "))
marks2 = float(input("Enter marks for Subject 2: "))
marks3 = float(input("Enter marks for Subject 3: "))
marks4 = float(input("Enter marks for Subject 4: "))
marks5 = float(input("Enter marks for Subject 5: "))

total_marks = marks1 + marks2 + marks3 + marks4 + marks5
percentage = (total_marks / 500) * 100

print("\n--- Marks Percentage Calculator ---")
print("Total Marks:", total_marks)
print("Percentage:", percentage, "%")
