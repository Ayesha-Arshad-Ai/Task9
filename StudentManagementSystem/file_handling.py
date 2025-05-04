import os

def read_students(file_path):
    """Reads student records from a text file."""
    students = []
    try:
        with open(file_path, 'r') as f:
            for line in f:
                parts = [p.strip() for p in line.split(',')]
                if len(parts) < 4:
                    continue  # skip malformed
                name, age, sid, *courses_str = parts
                courses = []
                for c in courses_str:
                    if ':' in c:
                        cn, cr = c.split(':')
                        courses.append((cn, int(cr)))
                students.append((name, int(age), sid, courses))
        print(f"Read {len(students)} students from {file_path}")
    except FileNotFoundError:
        print(f"Error: File {file_path} not found.")
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
    return students


def write_students(students, out_path):
    """Writes student records to a text file."""
    try:
        with open(out_path, 'w') as f:
            for name, age, sid, courses in students:
                course_parts = [f"{cn}:{cr}" for cn, cr in courses]
                line = ','.join([name, str(age), sid] + course_parts)
                f.write(line + '\n')
        print(f"Wrote {len(students)} students to {out_path}")
    except Exception as e:
        print(f"Error writing to {out_path}: {e}")

if __name__ == "__main__":
    data = read_students('students.txt')
    write_students(data, 'student_output.txt')