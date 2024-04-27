import "./style.css";
import { Link } from "react-router-dom";
import darkLogo from "../../assets/logo.png";
import lightLogo from "../../assets/light-logo.png"
import user from "../../assets/user.svg";
import { ToggleThemeBtn } from './../ToggleThemeBtn/index';
import { useContext } from "react";
import { ThemeContext } from "../themeContext";

export const Header = () => {
    const { mode } = useContext(ThemeContext);

    return (
        <div className="header">
            <div className="top_block" style={{background: mode === "light" ? "linear-gradient(180deg, #4B4848 0%, #1C1B1B 100%)" : "linear-gradient(180deg, #F1F1F1 0%, #999999 100%)"}}>
                <ToggleThemeBtn left="20px" top="50px"/>
                <img src={mode === 'light' ? darkLogo : lightLogo} className="mainLogo"/>
                <Link to="/login" className="userImage"><img src={user}/></Link>
            </div>
            <div className="bottom_block" style={{background: mode === "light" ? "#2A2A2A" : "#CCCCCC"}}>
                <ul className="navbar">
                    <li style={{color: mode === "light" ? "#FFF" : "#000"}}>Главная</li>
                    <li style={{color: mode === "light" ? "#FFF" : "#000"}}>Структура колледжа</li>
                    <li style={{color: mode === "light" ? "#FFF" : "#000"}}>Нормативные документы</li>
                    <li style={{color: mode === "light" ? "#FFF" : "#000"}}>Абитурентам</li>
                </ul>
            </div>
        </div>
    );
}
