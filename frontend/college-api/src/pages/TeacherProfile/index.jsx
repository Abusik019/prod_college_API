import "./style.css";

import axios from "axios";
import { Header } from '../../components/Header/index';
import { useContext, useEffect, useState } from "react";
import { ThemeContext } from "../../components/themeContext";
import getCookie from "../../components/GetCookie";
import { AboutExams } from '../../components/AboutExams';
import { AboutDisciplines } from './../../components/AboutDisciplines';
import { AboutLectures } from './../../components/AboutLectures';
import { TeacherLectures } from "../../components/AboutTeachers/AboutTeacher/TeacherLectures";
import { AboutGroups } from "../../components/AboutGroups";

function Profile() {
    const accessToken = getCookie("accessToken");
    const { mode } = useContext(ThemeContext);
    const [name, setName] = useState('');
    const [mainPageContent,  setMainPageContent] = useState('teachers');
   
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
                    <img src="https://static.mk.ru/upload/entities/2022/04/25/11/photoreportsImages/detailPicture/20/a0/4d/48/4e91f6aba4922221d9b24fbe54d17d02.jpg"/>
                    <div className="profile_info">
                        <h1>Важные ссылки</h1>
                        <div className="pr-line"></div> 
                    </div>
                        <div className="important_links-pr">
                        <button onClick={() => setMainPageContent('exams')}>Тесты</button>
                        <button onClick={() => setMainPageContent('disciplines')}>Специальности</button>
                        <button onClick={() => setMainPageContent('lectures')}>Лекции</button>
                        <button onClick={() => setMainPageContent('groups')}>Группы</button>
                    </div>
                </aside>
                <main className="profile_main">
                    <div className="pr-main-header-t">
                        <h1>Забит Ибрагимович<span>Махачкала, Дагестан</span></h1>
                        <h2><span>Специальность:</span> Информационные системы и программирование</h2>
                    </div>
                    <div className="pr-main-content-t">
                        {mainPageContent === 'exams' && <AboutExams />}
                        {mainPageContent === 'disciplines' && <AboutDisciplines />}
                        {mainPageContent === 'lectures' && <AboutLectures />}
                        {mainPageContent === 'groups' && <AboutGroups />}
                    </div>
                </main>
            </div>
        </div>
    )
}

export default Profile;
