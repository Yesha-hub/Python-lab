physics = int(input("Enter marks in Physics: "))
chemistry = int(input("Enter marks in Chemistry: "))
biology = int(input("Enter marks in Biology: "))
avg = (physics+chemistry+biology)/3
print("Average Marks: ", avg)
if avg >= 80:
    grade = "Distinction"
elif avg >= 60:
    grade = "First Division"
elif avg >= 45:
    grade = "Second Division"
elif avg >= 40:
    grade = "Pass"
else:
    grade = "Promotion not granted"
print("Grade:", grade)

output
Enter marks in Physics: 78
Enter marks in Chemistry: 88
Enter marks in Biology: 89
Average Marks:  85.0
Grade: Distinction
