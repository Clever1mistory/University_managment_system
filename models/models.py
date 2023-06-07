from datetime import datetime, date
from pydantic import BaseModel, Field


class Student(BaseModel):
    name: str
    email: str
    age: int
    group_id: int


class Teacher(BaseModel):
    id: int
    name: str
    email: str
    department_id: str


class Course(BaseModel):
    id: int
    name: str
    teacher_id: int
    faculty_id: int
    group_id: int


class Grade(BaseModel):
    id: int
    grade: float = Field(..., ge=2, le=5)
    student_id: int
    exam_id: int


class Group(BaseModel):
    id: int
    name: str
    department_id: int


class Department(BaseModel):
    id: int
    name: str
    faculty_id: int


class Schedule(BaseModel):
    id: int
    course_id: int
    day_of_week: int
    time_start: str
    time_end: str
    room_id: int
    course_id: int
    classroom_id: int


class Building(BaseModel):
    id: int
    name: str


class Classroom(BaseModel):
    id: int
    number: str
    building_id: int


class Semester(BaseModel):
    id: int
    name: str
    start_date: datetime
    end_date: datetime


class Faculty(BaseModel):
    id: int
    name: str


class Exam(BaseModel):
    id: int
    name: str
    date: date
    course_id: int


class IndependentWork(BaseModel):
    id: int
    name: str
    description: str
    given_date: datetime
    due_time: datetime
    course_id: int


class CourseProgram(BaseModel):
    id: int
    content: str
    course_id: int
    semester_id: int


class EduPlan(BaseModel):
    id: int
    name: str
    course_id: int
    semester_id: int
