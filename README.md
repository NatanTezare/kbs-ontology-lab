# 🎓 University Course Ontology — Knowledge-Based System Lab

🚀 **APT 3020: Knowledge Based Systems** — Practical Individual Lab  
United States International University-Africa  

---

## 📝 Project Description
This project implements a lightweight, structured **Domain Ontology** for a university academic ecosystem using Python object-oriented programming and logical dictionary mappings. 

In a Knowledge-Based System (KBS), an ontology provides the formal structure used to model real-world domains by defining explicit concepts (classes), individual instances (objects), relationships (object properties), and logical reasoning rules. This system models academic components at USIU-Africa and provides an inferencing layer to query operational data and evaluate course prerequisites dynamically.

---

## 🏛️ Ontology Core Architecture

### 1. Concepts & Structural Classes
The domain knowledge is encapsulated into **5 distinct classes**, each configured with specific data properties:

| Class Node | Purpose / Responsibility | Key Attributes Mapped |
| :--- | :--- | :--- |
| `Student` | Represents individuals enrolled in academic programs | `student_id`, `name`, `programme`, `year` |
| `Lecturer` | Represents faculty members responsible for instruction | `lecturer_id`, `name`, `department` |
| `Course` | Represents academic modules offered by the institution | `course_code`, `course_name`, `level` |
| `Department` | Represents structural academic divisions | `dept_code`, `name` |
| `Classroom` | Represents physical infrastructure locations | `room_id`, `capacity` |

### 2. Semantic Relationships
Entities are linked across the ontology framework using directional relational properties:
* **Student** ─── `enrolledIn` ───► **Course**
* **Lecturer** ─── `teaches` ───► **Course**
* **Course** ─── `belongsTo` ───► **Department**
* **Course** ─── `hasPrerequisite` ───► **Course**
* **Course** ─── `taughtIn` ───► **Classroom**

---

## 🧠 Reasoning & Query Layer
The system uses automated lookup logic to query facts and deduce downstream constraints without hardcoded entries. The following functional queries are implemented:

1. **`get_student_courses(student_name)`**: Inspects student enrollment sets.
2. **`get_course_lecturer(course_code)`**: Resolves faculty tracking for a specific module.
3. **`get_department_courses(dept_name)`**: Aggregates catalog listings belonging to a structural department.
4. **`get_students_in_course(course_code)`**: Inverts the enrollment graph to generate course rosters.
5. **`can_take_course(student_name, course_code)`**: An evaluation rule checking student history against prerequisite conditions to yield an approval decision.

---

## 🕹️ Execution Guide

To run the ontology interactive evaluation simulation, execute the control script from your shell environment:

```bash
python ontology_lab.py

```
👤 **Author:** Natan Abraham Tezare  



