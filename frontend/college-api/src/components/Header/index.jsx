import mainLogo from "../../assets/logo.png";
import user from "../../assets/user.svg";
import "./style.css";

export const Header = () => {
    return (
        <div className="header">
            <div className="top_block">
                <img src={mainLogo} className="mainLogo"/>
                <button className="userImage"><img src={user}/></button>
            </div>
            <div className="bottom_block">
                <ul className="navbar">
                    <li>Главная</li>
                    <li>Структура колледжа</li>
                    <li>Нормативные документы</li>
                    <li>Абитурентам</li>
                </ul>
            </div>
        </div>
    );
}
