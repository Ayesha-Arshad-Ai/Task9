"""Iterator and Generators for student tasks."""
import random
from SMS import Student

class StudentList:
    """Iterator over a list of Student objects."""
    def __init__(self, students):
        self._students = students
        self._index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self._index < len(self._students):
            student = self._students[self._index]
            self._index += 1
            return student
        raise StopIteration


def attendance_generator(students):
    """Yields daily attendance status (True/False) for each student."""
    for s in students:
        yield (s.name, random.choice([True, False]))


def random_marks_generator(students):
    """Yields a random mark (0-100) for each student."""
    for s in students:
        yield (s.name, random.randint(0,100))

if __name__ == "__main__":
    # sample students
    s1 = Student("Dan", 21, "S4001", courses=[("Hist",2)], grades={"Hist":75})
    s2 = Student("Eve", 20, "S4002", courses=[("Math",3)], grades={"Math":82})
    sl = StudentList([s1, s2])
    print("Iterating students:")
    for student in sl:
        print(student.name)

    print("\nDaily Attendance:")
    for name, present in attendance_generator([s1,s2]):
        print(f"{name}: {'Present' if present else 'Absent'}")

    print("\nRandom Marks:")
    for name, mark in random_marks_generator([s1,s2]):
        print(f"{name}: {mark}")
