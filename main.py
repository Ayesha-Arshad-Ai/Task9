"""Demonstrates usage of student_utils package."""
from student_utils.arithmetic import percentage, classify_grade
from student_utils.attendance import attendance_percentage
from student_utils.performance import evaluate_performance

if __name__ == "__main__":
    marks = [85, 90, 78]
    pct = percentage(marks)
    print(f"Percentage: {pct}%")
    grades = [classify_grade(m) for m in marks]
    print(f"Letter Grades: {grades}")

    attend = attendance_percentage(45, 50)
    print(f"Attendance: {attend}%")

    from SMS import Student
    s = Student("Carol", 22, "S3001", courses=[("Eng",3)], grades={"Eng":88})
    gpa = s.calculate_gpa()
    perf = evaluate_performance(gpa)
    print(f"GPA: {gpa}, Performance: {perf}")