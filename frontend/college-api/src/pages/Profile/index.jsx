import "./style.css";

import axios from "axios";
import { Header } from './../../components/Header/index';
import { useContext, useEffect, useState } from "react";
import { ThemeContext } from "../../components/themeContext";
import getCookie from "../../components/GetCookie";

function Profile() {
    const accessToken = getCookie("accessToken");
    const { mode } = useContext(ThemeContext);
    const [name, setName] = useState('');

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
                            <button>Экзамены</button>
                            <button>Расписание</button>
                            <button>Преподаватели</button>
                            <button>Учебный процесс</button>
                        </div>
                </aside>
                <main className="profile_main">
                    <div className="pr-main-header">
                        <h1>Забит Ибрагимов<span>Махачкала, Дагестан</span></h1>
                    </div>
                    <div className="pr-main-content"></div>
                </main>
            </div>
        </div>
    )
}

export default Profile;
