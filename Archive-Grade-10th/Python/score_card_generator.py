print("Report Card Generator")

name = input("Enter student name: ")
math = int(input("Enter Math marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

average = (math + science + english) / 3

if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 50:
    grade = "C"
else:
    grade = "D"

print("\n--- Report Card ---")
print("Name:", name)
print("Math:", math)
print("Science:", science)
print("English:", english)
print("Average:", average)
print("Grade:", grade)
