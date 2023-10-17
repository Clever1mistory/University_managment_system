## "Система управления университетом"

# Данный проект представляет собой схематичную систему управления университетскими делами. По сути своей являющийся концептом для дальнейшей полноценной разработки
# Проектирование БД в виде ER-диаграмм выполнено в https://drawsql.app/
*Установка и запуск:*
В терминале: 
`git clone <git репозиторий>`
`pip install -r requirements.txt`
Для запуска: `uvicorn main:app --reload`
Проверить работоспособность API можно проверить по адресу: http://localhost:8000/docs

![Аннотация 2023-06-07 153239](https://github.com/Clever1mistory/University_managment_system/assets/128373879/129cd0f9-3f3c-45ef-a120-55ce2adfa645)



# 1. База данных. Создание сущностей
<html>
<body>
<p>
Сущность "Студент":
<br> - Идентификатор (id) - целочисленное значение, автоинкрементируемое;
<br> - Имя (name) - текстовое значение;
<br> - Номер группы (group_id) - целочисленное значение, foreign key на таблицу "Группа".
</p>
<p>
Сущность "Преподаватель":
<br> - Идентификатор (id) - целочисленное значение, автоинкрементируемое;
<br> - Имя (name) - текстовое значение;
<br> - Возраст (age) – целочисленное значение;
<br> - Номер отделения (department_id) - целочисленное значение, foreign key на таблицу "Отделение".
</p>
<p>
Сущность "Курс":
<br> - Идентификатор (id) - целочисленное значение, автоинкрементируемое;
<br> - Название (name) - текстовое значение;
<br> - Номер факультета (faculty_id) - целочисленное значение, foreign key на таблицу "Факультет";
<br> - Номер группы (group_id) - целочисленное значение, foreign key на таблицу "Группа".
</p>
<p>
Сущность "Группа":
<br> - Идентификатор (id) - целочисленное значение, автоинкрементируемое;
<br> - Название (name) - текстовое значение;
<br> - Номер отделения (department_id) - целочисленное значение, foreign key на таблицу "Отделение".
</p>
<p>
Сущность "Отделение":
<br> - Идентификатор (id) - целочисленное значение, автоинкрементируемое;
<br> - Название (name) - текстовое значение;
<br> - Номер факультета (faculty_id) - целочисленное значение, foreign key на таблицу "Факультет".
</p>
<p>
Сущность "Оценка":
<br> - Идентификатор (id) - целочисленное значение, автоинкрементируемое;
<br> - Значение (value) - целочисленное значение;
<br> - Идентификатор студента (student_id) - целочисленное значение, foreign key на таблицу "Студент";
<br> - Идентификатор экзамена (exam_id) - целочисленное значение, foreign key на таблицу "Экзамен".
</p>
<p>
Сущность "Расписание":
<br> - Идентификатор (id) - целочисленное значение, автоинкрементируемое;
<br> - День недели (day_of_week) - целочисленное значение;
<br> - Время начала (start_time) - время, формат: ЧЧ:ММ:СС;
<br> - Дата начала (start_date) - дата, формат: ГГГГ-ММ-ДД;
<br> - Идентификатор курса (course_id) - целочисленное значение, foreign key на таблицу "Курс";
<br> - Идентификатор группы (group_id) - целочисленное значение, foreign key на таблицу "Группа";
<br> - Идентификатор аудитории (classroom_id) - целочисленное значение, foreign key на таблицу "Аудитория".
</p>
<p>
Сущность "Здание":
<br> - Идентификатор (id) - целочисленное значение, автоинкрементируемое;
<br> - Название (name) - текстовое значение.
</p>
<p>
Сущность "Аудитория":
<br> - Идентификатор (id) - целочисленное значение, автоинкрементируемое;
<br> - Номер (number) - текстовое значение;
<br> - Идентификатор здания (building_id) - целочисленное значение, foreign key на таблицу "Здание".
</p>
<p>
Сущность "Семестр":
<br> - Идентификатор (id) - целочисленное значение, автоинкрементируемое;
<br> - Название (name) - текстовое значение;
<br> - Дата начала (start_date) - дата, формат: ГГГГ-ММ-ДД;
<br> - Дата окончания (end_date) - дата, формат: ГГГГ-ММ-ДД.
</p>
<p>
Сущность "Факультет":
<br> - Идентификатор (id) - целочисленное значение, автоинкрементируемое;
<br> - Название (name) - текстовое значение.
</p>
<p>
Сущность "Экзамен":
<br> - Идентификатор (id) - целочисленное значение, автоинкрементируемое;
<br> - Название (name) - текстовое значение;
<br> - Идентификатор курса (course_id) - целочисленное значение, foreign key на таблицу "Курс";
<br> - Дата (date) - дата, формат: ГГГГ-ММ-ДД.
</p>
<p>
Сущность "Задание для самостоятельной работы":
<br> - Идентификатор (id) - целочисленное значение, автоинкрементируемое;
<br> - Название (name) - текстовое значение;
<br> - Описание (description) - текстовое значение;
<br> - Дата выдачи (given_date) - дата, формат: ГГГГ-ММ-ДД;
<br> - Дата сдачи (due_date) - дата, формат: ГГГГ-ММ-ДД;
<br> - Идентификатор курса (course_id) - целочисленное значение, foreign key на таблицу "Курс".
</p>
<p>
Сущность
"Программа курса":
<br> - Идентификатор (id) - целочисленное значение, автоинкрементируемое;
<br> - Название (name) - текстовое значение;
<br> - Идентификатор семестра (semester_id) - целочисленное значение, foreign key на таблицу "Семестр".
<br> - Идентификатор курса (course_id) - целочисленное значение, foreign key на таблицу "Курс".
</p>
<p>
Сущность "Учебный план":
<br> - Идентификатор (id) - целочисленное значение, автоинкрементируемое;
<br> - Название (name) - текстовое значение;
<br> - Идентификатор курса (course_id) - целочисленное значение, foreign key на таблицу "Курс".
</p>
</body>
</html>
# 2. SQL запросы
SQL скрипты для создания таблиц:

CREATE TABLE student (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
group_id INTEGER NOT NULL,
FOREIGN KEY (group_id) REFERENCES group (id)
);

CREATE TABLE teacher (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INTEGER NOT NULL,
department_id INTEGER NOT NULL,
FOREIGN KEY (department_id) REFERENCES department (id)
);

CREATE TABLE course (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
faculty_id INTEGER NOT NULL,
group_id INTEGER NOT NULL,
FOREIGN KEY (faculty_id) REFERENCES faculty (id),
FOREIGN KEY (group_id) REFERENCES group (id)
);

CREATE TABLE group (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
department_id INTEGER NOT NULL,
FOREIGN KEY (department_id) REFERENCES department (id)
);

CREATE TABLE department (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
faculty_id INTEGER NOT NULL,
FOREIGN KEY (faculty_id) REFERENCES faculty (id)
);

CREATE TABLE grade (
id INTEGER PRIMARY KEY AUTOINCREMENT,
value INTEGER NOT NULL,
student_id INTEGER NOT NULL,
exam_id INTEGER NOT NULL,
FOREIGN KEY (student_id) REFERENCES student (id),
FOREIGN KEY (exam_id) REFERENCES exam (id)
);

CREATE TABLE schedule (
id INTEGER PRIMARY KEY AUTOINCREMENT,
day_of_week INTEGER NOT NULL,
start_time TIME NOT NULL,
start_date DATE NOT NULL,
course_id INTEGER NOT NULL,
group_id INTEGER NOT NULL,
classroom_id INTEGER NOT NULL,
FOREIGN KEY (course_id) REFERENCES course (id),
FOREIGN KEY (group_id) REFERENCES group (id),
FOREIGN KEY (classroom_id) REFERENCES classroom (id)
);

CREATE TABLE building (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL
);

CREATE TABLE classroom (
id INTEGER PRIMARY KEY AUTOINCREMENT,
number TEXT NOT NULL,
building_id INTEGER NOT NULL,
FOREIGN KEY (building_id) REFERENCES building (id)
);

CREATE TABLE semester (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
start_date DATE NOT NULL,
end_date DATE NOT NULL
);

CREATE TABLE faculty (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL
);

CREATE TABLE exam (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
course_id INTEGER NOT NULL,
date DATE NOT NULL,
FOREIGN KEY (course_id) REFERENCES course (id)
);

CREATE TABLE indepwork (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
description TEXT NOT NULL,
given_date DATE NOT NULL,
due_date DATE NOT NULL,
course_id INTEGER NOT NULL,
FOREIGN KEY (course_id) REFERENCES course (id)
);

CREATE TABLE course_program (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
semester_id INTEGER NOT NULL,
course_id INTEGER NOT NULL,
FOREIGN KEY (semester_id) REFERENCES semester (id),
FOREIGN KEY (course_id) REFERENCES course (id)
);

CREATE TABLE eduplan (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
faculty_id INTEGER NOT NULL,
semester_id INTEGER NOT NULL,
FOREIGN KEY (faculty_id) REFERENCES faculty (id),
FOREIGN KEY (semester_id) REFERENCES semester (id)
);
![drawSQL-first-univ-export-2023-06-07](https://github.com/Clever1mistory/University_managment_system/assets/128373879/a94ce03b-c7ee-46d0-a4e6-9d6a7fd4728b)


