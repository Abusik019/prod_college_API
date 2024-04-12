<div align="center"><img src='https://law.dgu.ru/college/styles/img/logo2.jpg'></div>

<h1 align="center">API сайта колледжа ДГУ</h1>

<center><b>Стек бэкенда:</b></center>     

<div>
    <img src="https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray">
    <img src="https://img.shields.io/badge/Celery-37814A.svg?style=for-the-badge&logo=Celery&logoColor=white">
    <img src="https://img.shields.io/badge/PostgreSQL-4169E1.svg?style=for-the-badge&logo=PostgreSQL&logoColor=white">
    <img src="https://img.shields.io/badge/Redis-DC382D.svg?style=for-the-badge&logo=Redis&logoColor=white">
    <img src="https://img.shields.io/badge/Docker-2496ED.svg?style=for-the-badge&logo=Docker&logoColor=white">
    <img src="https://img.shields.io/badge/Postman-FF6C37.svg?style=for-the-badge&logo=Postman&logoColor=white">
    <img src="https://img.shields.io/badge/-Linux-185885?logo=linux&style=for-the-badge&logoColor=fff">
    <img src="https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white">
    <img src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white">
</div>

---

**Демо-версия, сайт разрабатывается по нашей инициативе, сайт разрабатывают:**

- Ибрагимов Забит (Backend Developer)
- Гасанбеков Абужапар (Frontend Developer)
- Курбаналиева Альфия (UI-UX Designer)

---

<h1 align="center">Функционал</h1>

**users**
- Авторизация (JWT)
- Список всех пользователей
- Получение данных отдельного пользователя
- Обновление информации профиля(email, photo)

**Students**
- Получение списка студентов
- Получение информации отдельного студента
- Получение группы студента

**Teachers**
- Получение списка преподавателей
- Получение информации отдельного препода
- Получение всех групп препода
- Изменение групп в которых преподает учитель
- Изменение предметов которые ведет препод

**lectures**
- Получение списка лекций препода
- Получение информации отдельной лекции
- Просмотр собственных лекций
- Изменение лекции
- Создание лекции
- Удаление лекции

**Groups**
- Получение списка всех групп
- Просмотр членов группы (одногруппники, преподы)

**News**
- Получение списка новостей
- Получение информации отдельной новости
- Создание, удаление, изменение через админку

**Reviews**
- Получение списка отзывов под отдельной лекцией
- Создание отзыва
- Удаление отзыва

**Exams**
- Начало экзамена (получение вопросов(в рандомном порядке) и ответов, при старте препод получает уведомление)
- Завершение экзамена (Получение оценки из среднеарифметического, уведомление на почту препода и занесение результата в таблицу Results)
- Получение списка экзаменов препода
- Получение списка экзаменов для студента
- Создание экзамена (По его истечению свойство "ended" меняется на True и экзамен становится недоступным)
- Изменение экзамена
- Удаление экзамена

**Results**
- Получение результатов экзаменов для студента
- Получение результатов экзаменов учителя

Новый функционал еще будет добавляться

---

<h1 align="center">Схема БД</h1>

<img src='https://i.ibb.co/2nLHGG0/Copy-of-Untitled-Diagram.png'>
