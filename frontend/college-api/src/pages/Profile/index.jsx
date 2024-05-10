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
    const [mainPageContent,  setMainPageContent] = useState('teachers');
    console.log(mainPageContent);
   
    const headers = {
        'Authorization': `Bearer ${accessToken}`,
        'Content-Type': 'application/json'
      };

    // useEffect(() => {
    //     axios.get("https://d7a6-185-244-21-185.ngrok-free.app/api/v1/users/current_user", { headers })
    //         .then((response) => {
    //             console.log(response);
    //             setName(response.data.first_name);
    //         })
    //         .catch((error) => {
    //             console.log(error);
    //         });
    // })


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
                        <button onClick={() => setMainPageContent('exams')}>Экзамены</button>
                        <button onClick={() => setMainPageContent('schedule')}>Расписание</button>
                        <button onClick={() => setMainPageContent('teachers')}>Преподаватели</button>
                        <button onClick={() => setMainPageContent('educ_process')}>Учебный процесс</button>
                    </div>
                </aside>
                <main className="profile_main">
                    <div className="pr-main-header">
                        <h1>Забит Ибрагимов<span>Махачкала, Дагестан</span></h1>
                        <h2><span>Направление:</span> Информационные системы и программирование</h2>
                        <h3><span>Курс:</span> 3</h3>
                        <h4><span>Группа:</span> 1</h4>
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
