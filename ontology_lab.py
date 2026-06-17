# Part A: Define Ontology Classes
class Student:
    def __init__(self, student_id, name, programme, year):
        self.student_id = student_id
        self.name = name
        self.programme = programme
        self.year = year

class Lecturer:
    def __init__(self, lecturer_id, name, department):
        self.lecturer_id = lecturer_id
        self.name = name
        self.department = department

class Course:
    def __init__(self, course_code, course_name, level):
        self.course_code = course_code
        self.course_name = course_name
        self.level = level

class Department:
    def __init__(self, dept_code, name):
        self.dept_code = dept_code
        self.name = name

class Classroom:
    def __init__(self, room_id, capacity):
        self.room_id = room_id
        self.capacity = capacity

# Part B: Create Ontology Objects
# 5 Students
s1 = Student("S001", "Mary", "Applied Computer Technology", 2)
s2 = Student("S002", "Brian", "Computer Science", 3)
s3 = Student("S003", "Linda", "Information Systems", 2)
s4 = Student("S004", "Natan", "Computer Science", 3)
s5 = Student("S005", "Videlis", "Computer Science", 3)

# 3 Lecturers
l1 = Lecturer("L001", "Dr. Otieno", "Computer Science")
l2 = Lecturer("L002", "Dr. Smith", "Mathematics")
l3 = Lecturer("L003", "Prof. Jane", "Computer Science")

# 5 Courses
c1 = Course("APT3020", "Knowledge Based Systems", 3)
c2 = Course("IST4040", "Information Systems Audit", 4)
c3 = Course("APT4040", "Artificial Intelligence", 4)
c4 = Course("CSC1010", "Introduction to Programming", 1)
c5 = Course("MTH2010", "Calculus II", 2)

# 2 Departments
d1 = Department("D01", "Computer Science")
d2 = Department("D02", "Mathematics")

# 3 Classrooms
cr1 = Classroom("SCB1", 40)
cr2 = Classroom("SCB2", 35)
cr3 = Classroom("LAB1", 30)

# Part C: Create Relationships
enrollments = {
    "Mary": ["APT3020", "IST4040"],
    "Brian": ["APT3020", "CSC1010"],
    "Linda": ["APT3020"],
    "Natan": ["APT3020", "APT4040"],
    "Videlis": ["IST4040"]
}

# Tracking completed courses specifically to handle the prerequisite logic test
completed_courses = {
    "Mary": ["CSC1010"] 
}

course_lecturer = {
    "APT3020": "Dr. Otieno",
    "IST4040": "Dr. Smith",
    "APT4040": "Prof. Jane",
    "CSC1010": "Dr. Otieno",
    "MTH2010": "Dr. Smith"
}

department_courses = {
    "Computer Science": ["APT3020", "IST4040", "APT4040", "CSC1010"],
    "Mathematics": ["MTH2010"]
}

prerequisites = {
    "APT4040": "APT3020",
    "APT3020": "CSC1010",
    "IST4040": None,
    "CSC1010": None,
    "MTH2010": None
}

taught_in = {
    "APT3020": "LAB1",
    "IST4040": "SCB1",
    "APT4040": "LAB1",
    "CSC1010": "SCB2",
    "MTH2010": "SCB1"
}

# Part D: Add Reasoning Functions
def get_student_courses(student_name):
    courses = enrollments.get(student_name, [])
    print(f"Courses taken by {student_name}:")
    for c in courses:
        print(f"- {c}")
    print()

def get_course_lecturer(course_code):
    lecturer = course_lecturer.get(course_code, "Unknown")
    print(f"Lecturer teaching {course_code}:")
    print(f"- {lecturer}")
    print()

def get_department_courses(dept_name):
    courses = department_courses.get(dept_name, [])
    print(f"Courses in {dept_name} Department:")
    for c in courses:
        print(f"- {c}")
    print()

def get_students_in_course(course_code):
    students = []
    for student, courses in enrollments.items():
        if course_code in courses:
            students.append(student)
    print(f"Students taking {course_code}:")
    for s in students:
        print(f"- {s}")
    print()

def can_take_course(student_name, course_code):
    prereq = prerequisites.get(course_code)
    print(f"Can {student_name} take {course_code}?")
    if prereq:
        completed = completed_courses.get(student_name, [])
        if prereq not in completed:
            print(f"No. Missing prerequisite: {prereq}")
            print()
            return False
    print("Yes.")
    print()
    return True

# 6. Minimum Expected Output Execution
if __name__ == "__main__":
    get_student_courses("Mary")
    get_course_lecturer("APT3020")
    get_department_courses("Computer Science")
    get_students_in_course("APT3020")
    can_take_course("Mary", "APT4040")