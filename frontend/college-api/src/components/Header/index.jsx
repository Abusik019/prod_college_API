import "./style.css";
import { Link } from "react-router-dom";
import darkLogo from "../../assets/logo.png";
import lightLogo from "../../assets/light-logo.png"
import user from "../../assets/user.svg";
import { ToggleThemeBtn } from './../ToggleThemeBtn/index';
import { useContext, useEffect, useState } from "react";
import { ThemeContext } from "../themeContext";
import getCookie from './../GetCookie/index';
import axios from "axios";

export const Header = () => {
    const { mode } = useContext(ThemeContext);
    const accessToken = getCookie('accessToken')
    const [isTeacher, setIsTeacher] = useState(false);
    const headers = {
        Authorization: `Bearer ${accessToken}`,
        "Content-Type": "application/json",
    };

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/v1/users/current_user", { headers })
            .then((response) => {
                setIsTeacher(response.data.is_teacher);
            })
            .catch((error) => {
                console.log(error);
            });
    }, []);

    return (
        <div className="header">
            <div className="top_block" style={{background: mode === "light" ? "linear-gradient(180deg, #4B4848 0%, #1C1B1B 100%)" : "linear-gradient(180deg, #F1F1F1 0%, #999999 100%)"}}>
                <ToggleThemeBtn left="20px" top="50px"/>
                <Link to="/">
                    <img
                        src={mode === "light" ? darkLogo : lightLogo}
                        className="mainLogo"
                    />
                </Link>
                <Link to={getCookie('accessToken') ? isTeacher ? '/teacher-profile' : '/profile' : 'login'} className="userImage"><img src={user}/></Link>
            </div>
            <div className="bottom_block" style={{background: mode === "light" ? "#2A2A2A" : "#CCCCCC"}}>
                <ul className="navbar">
                    <Link to='/'><li style={{color: mode === "light" ? "#FFF" : "#000"}}>Главная</li></Link>
                    <Link to='/structure'><li style={{color: mode === "light" ? "#FFF" : "#000"}}>Структура колледжа</li></Link>
                    <Link to='/documents'><li style={{color: mode === "light" ? "#FFF" : "#000"}}>Нормативные документы</li></Link>
                    <Link to='/applicants'><li style={{color: mode === "light" ? "#FFF" : "#000"}}>Абитуриентам</li></Link>
                </ul>
            </div>
        </div>
    );
}
