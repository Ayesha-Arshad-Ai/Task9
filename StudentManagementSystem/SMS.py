class Student:
    def __init__(self, name, age, student_id, courses=None, grades=None):
        self._name = name
        self._age = age
        self._student_id = student_id
        self._courses = courses or []            # list of (course_name, credit)
        self._grades = grades or {}              # dict course_name -> grade (0-100)

    # Getters and setters
    @property
    def name(self): return self._name
    @name.setter
    def name(self, value): self._name = value

    @property
    def age(self): return self._age
    @age.setter
    def age(self, value): self._age = value

    @property
    def student_id(self): return self._student_id
    @student_id.setter
    def student_id(self, value): self._student_id = value

    @property
    def courses(self): return self._courses
    @courses.setter
    def courses(self, value): self._courses = value

    @property
    def grades(self): return self._grades
    @grades.setter
    def grades(self, value): self._grades = value

    def calculate_gpa(self):
        """
        Calculates GPA on a 4.0 scale assuming grades are 0-100.
        GPA = sum((grade/100)*4.0 * credit for each course) / total_credits
        """
        total_credits = sum(credit for _, credit in self._courses)
        if total_credits == 0:
            return 0.0
        quality_points = 0.0
        for course, credit in self._courses:
            grade = self._grades.get(course, 0)
            quality_points += (grade / 100.0) * 4.0 * credit
        return round(quality_points / total_credits, 2)

    def __str__(self):
        info = f"Student ID: {self._student_id}\n"
        info += f"Name: {self._name}, Age: {self._age}\n"
        info += f"Courses: {', '.join(c for c,_ in self._courses)}\n"
        info += f"GPA: {self.calculate_gpa()}"
        return info

class GraduateStudent(Student):
    def __init__(self, name, age, student_id, thesis_title, courses=None, grades=None):
        super().__init__(name, age, student_id, courses, grades)
        self._thesis_title = thesis_title

    @property
    def thesis_title(self): return self._thesis_title
    @thesis_title.setter
    def thesis_title(self, value): self._thesis_title = value

    def __str__(self):
        base = super().__str__()
        return f"{base}\nThesis Title: {self._thesis_title}"

# Demonstration
if __name__ == "__main__":
    student = Student("Alice", 20, "S1001", courses=[("Math",3), ("Bio",4)], grades={"Math":85, "Bio":90})
    print(student)
    grad = GraduateStudent("Bob", 24, "G2001", thesis_title="AI in Healthcare",
                           courses=[("ML",3), ("Stats",3)], grades={"ML":88, "Stats":92})
    print("\n" + str(grad))

