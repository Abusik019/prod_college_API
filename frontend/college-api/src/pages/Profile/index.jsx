import "./style.css";

import axios from "axios";
import { Header } from './../../components/Header/index';
import { useContext, useEffect, useState } from "react";
import { ThemeContext } from "../../components/themeContext";
import getCookie from "../../components/GetCookie";
import { AboutTeachers } from "../../components/AboutTeachers";
import { AboutExams } from './../../components/AboutExams';
import { AboutSchedule } from "../../components/AboutSchedule";
import { AboutEducProcess } from './../../components/AboutEducProcess';
import { TeacherLectures } from "../../components/AboutTeachers/AboutTeacher/TeacherLectures";

function Profile() {
    const accessToken = getCookie("accessToken");
    const { mode } = useContext(ThemeContext);
    const [name, setName] = useState('');
    const [surname, setSurname] = useState('');
    const [facult, setFacult] = useState('');
    const [group, setGroup] = useState('');
    const [course, setCourse] = useState('');
    const [mainPageContent,  setMainPageContent] = useState('teachers');
   
    const headers = {
        'Authorization': `Bearer ${accessToken}`,
        'Content-Type': 'application/json'
    };

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/v1/users/current_user", { headers })
            .then((response) => {
                console.log(response);
                setName(response.data.first_name);
                setSurname(response.data.last_name);
                setFacult(response.data.group.facult_name);
                setGroup(response.data.group.course_name);
                setCourse(response.data.group.podgroup_name);
            })
            .catch((error) => {
                console.log(error);
            });
    })


    return (
        <div className="profile" style={{background: mode === "light"  ? "#313131" : "#E7E7E7"}}>
            <Header />
            <div className="profile_container">
                <aside className="profile_aside">
                    <img src="https://hips.hearstapps.com/hmg-prod/images/leonardo-dicaprio-attends-the-killers-of-the-flower-moon-news-photo-1692286498.jpg?crop=0.908xw:0.605xh;0.0522xw,0.0542xh&resize=640:*"/>
                    <div className="profile_info">
                        <h1>Важные ссылки</h1>
                        <div className="pr-line"></div>
                    </div>
                        <div className="important_links-pr">
                        <button onClick={() => setMainPageContent('exams')}>Тесты</button>
                        <button onClick={() => setMainPageContent('schedule')}>Расписание</button>
                        <button onClick={() => setMainPageContent('teachers')}>Преподаватели</button>
                        <button onClick={() => setMainPageContent('educ_process')}>Учебный процесс</button>
                    </div>
                </aside>
                <main className="profile_main">
                    <div className="pr-main-header">
                        <h1>{name} {surname}<span>Махачкала, Дагестан</span></h1>
                        <h2><span>Направление:</span> {facult}</h2>
                        <h3><span>Курс:</span> {group}</h3>
                        <h4><span>Группа:</span> {course}</h4>
                    </div>
                    <div className="pr-main-content">
                        {mainPageContent === 'teachers' && <AboutTeachers />}
                        {mainPageContent === 'exams' && <AboutExams />}
                        {mainPageContent === 'schedule' && <AboutSchedule />}
                        {mainPageContent === 'educ_process' && <AboutEducProcess />}
                    </div>
                </main>
            </div>
        </div>
    )
}

export default Profile;
