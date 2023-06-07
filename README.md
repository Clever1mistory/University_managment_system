
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

![drawSQL-first-univ-export-2023-06-07](https://github.com/Clever1mistory/University-managment-systems/assets/128373879/cae74521-3ed2-421b-a6fc-a4e2579bfb21)
