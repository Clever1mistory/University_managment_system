from datetime import date

from fastapi import FastAPI, HTTPException
from models.models import Student, Teacher, Course, Grade, Exam


app = FastAPI()


students_db = [
    Student(id=1, name="Alice", email='alice@gmail.com', age=18, group_id=1),
    Student(id=2, name="Bob", email='bobo@gmail.com', age=18, group_id=1),
    Student(id=3, name="Charlie", email='charlzy@gmail.com', age=20, group_id=2),
]

teachers_db = [
    Teacher(id=1, name="Драгомир Сергеевич", email='drago@gmail.com', department_id=1),
    Teacher(id=2, name="Николай Николаевич", email='kolya@gmail.com', department_id=2),
]

courses_db = [
    Course(id=1, name="Math", teacher_id=1, faculty_id=1, group_id=1),
    Course(id=2, name="Physics", teacher_id=1, faculty_id=1, group_id=2),
    Course(id=3, name="Programming", teacher_id=2, faculty_id=2, group_id=1),
]

grades_db = [
    Grade(id=1, grade=3, student_id=1, exam_id=1),
    Grade(id=2, grade=4, student_id=1, exam_id=2),
    Grade(id=3, grade=5, student_id=2, exam_id=1),
]

exams_db = [
    Exam(id=1, name='Math', date=date.today(), course_id=1),
    Exam(id=2, name='Physics', date=date.today(), course_id=2),
    Exam(id=3, name='Programming', date=date.today(), course_id=3),
]


@app.post("/students")
async def create_student(student: Student):
    students_db.append(student)
    return student


@app.get("/students/{student_id}")
async def read_student(student_id: int):
    for student in students_db:
        if student.id == student_id:
            return student
    raise HTTPException(status_code=404, detail='Студент не найден')


@app.put("/students/{student_id}")
async def update_student(student_id: int, student: Student):
    for i, s in enumerate(students_db):
        if s.id == student_id:
            students_db[i] = student
            return student
    raise HTTPException(status_code=404, detail='Студент не найден')


@app.delete("/students/{student_id}")
async def delete_student(student_id: int):
    for i, student in enumerate(students_db):
        if student.id == student_id:
            del students_db[i]
            return {'message': 'Удаление прошло успешно'}
    raise HTTPException(status_code=404, detail='Студент не найден')


@app.get("/teachers")
async def read_teachers():
    return teachers_db


@app.post("/courses")
async def create_course(course: Course):
    courses_db.append(course)
    return course


@app.get("/courses/{course_id}")
async def read_course(course_id: int):
    for course in courses_db:
        if course.id == course_id:
            return course
    raise HTTPException(status_code=404, detail='Курс не найден')


@app.get("/courses/{course_id}/students")
async def read_course_students(course_id: int):
    students_on_course = []
    for grade in grades_db:
        if grade.course_id == course_id:
            for student in students_db:
                if student.id == grade.student_id:
                    students_on_course.append(student)
    return students_on_course


@app.post("/grades")
async def create_grade(grade: Grade):
    grades_db.append(grade)
    return grade


@app.put("/grades/{grade_id}")
async def update_grade(grade_id: int, grade: Grade):
    for i, g in enumerate(grades_db):
        if g.id == grade_id:
            grades_db[i] = grade
            return grade
    raise HTTPException(status_code=404, detail='Оценка не найдена')

