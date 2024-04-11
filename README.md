<div><img src='https://law.dgu.ru/college/styles/img/logo2.jpg'></div>

<center><h1>API сайта колледжа ДГУ</h1></center>
<hr>
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
<hr>

<b>Демо-версия, сайт разработан по нашей инициативе, сайт разрабатывали:</b>
<ul>
    <li> Ибрагимов Забит (Backend Developer)
    <li> Гасанбеков Абужапар (Frontend Developer)
    <li> Курбаналиева Альфия (UI-UX Designer)
</ul>

<hr>

<center><h1>Функционал</h1></center>
<b>users
<ul>
    <li> Авторизация (JWT)
    <li> Список всех пользователей
    <li> Получение данных отдельного пользователя
    <li> Обновление информации профиля(email, photo)
</ul>
<b>Students
<ul>
    <li> Получение списка студентов
    <li> Получение информации отдельного студента
    <li> Получение группы студента
</ul>
<b>Teachers
<ul>
    <li> Получение списка преподавателей
    <li> Получение информации отдельного препода
    <li> Получение всех групп препода
    <li> Изменение групп в которых преподает учитель
    <li> Изменение предметов которые ведет препод
</ul>
<b>lectures
<ul>
    <li> Получение списка лекций препода
    <li> Получение информации отдельного лекции
    <li> Просмотр собственных лекций
    <li> Изменение лекции
    <li> Создание лекции
    <li> Удаление лекции
</ul>
<b>Groups
<ul>
    <li> Получение списка всех групп
    <li> Просмотр членов группы (одногруппники, преподы)
</ul>
<b>News
<ul>
    <li> Получение списка новостей
    <li> Получение информации отдельной новости
    <li> Создание, удаление, изменение через админку
</ul>
<b>Reviews
<ul>
    <li> Получение списка отзывов под отдельной лекцией
    <li> Создание отзыва
    <li> Удаление отзыва
</ul>
<b>Exams
<ul>
    <li> Начало экзамена (получение вопросов(в рандомном порядке) и ответов, при старте препод получает уведомление)
    <li> Завершение экзамена (Получение оценки из среднеарифметического, уведомление на почту препода и занесение результата в таблицу Results)
    <li> Получение списка экзаменов препода
    <li> Получение списка экзаменов для студента
    <li> Создание экзамена (По его истечению свойство "ended" меняется на True и экзамен становится не доступным)
    <li> Изменение экзамена
    <li> Удаление экзамена
</ul>
<b>Results
<ul>
    <li> Получение результатов экзаменов для студента
    <li> Получение результатов экзаменов учителя
</ul>
<p>
новый функционал еще будет добавляться
<hr>
<center><h1>Схема БД</h1></center>
<img src='https://i.ibb.co/2nLHGG0/Copy-of-Untitled-Diagram.png'>
