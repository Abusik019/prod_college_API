import "./style.css";
import darkLogo from "../../assets/logo.png";
import lightLogo from "../../assets/light-logo.png";
import { Link } from "react-router-dom";
import { useContext } from "react";
import { ThemeContext } from "../../components/themeContext";
import { ToggleThemeBtn } from "../../components/ToggleThemeBtn";
import darkUser from "../../assets/darkuser.png";
import lightUser from "../../assets/lightuser.png";

export default function Login() {
    const { mode } = useContext(ThemeContext);

    return (
        <div
            className="login"
            style={{ background: mode === "light" ? "#313131" : "#E7E7E7" }}
        >
            <div
                className="login_head"
                style={{
                    background:
                        mode === "light"
                            ? "linear-gradient(180deg, #4B4848 0%, #1C1B1B 100%)"
                            : "linear-gradient(180deg, #F1F1F1 0%, #999999 100%)",
                }}
            >
                <ToggleThemeBtn left="20px" top="50px" />
                <Link to="/">
                    <img
                        src={mode === "light" ? darkLogo : lightLogo}
                        className="mainLogo"
                    />
                </Link>
            </div>

            <div className="loginFormContainer">
                <div className="shape first"></div>
                <div className="shape second"></div>

                <form className="loginForm">
                    <div className="imageWrapper"><img src={mode === "light" ? lightUser : darkUser}/></div>
                    <label htmlFor="username" style={{ color: mode === "light" ? "#fff" : "#000" }}>
                        Имя
                        <input
                            type="text"
                            placeholder="Имя"
                            id="username"
                            style={{ color: mode === "light" ? "#fff" : "#000" }}
                        />
                    </label>
                    <label htmlFor="password" style={{ color: mode === "light" ? "#fff" : "#000" }}>
                        Фамилия
                        <input
                            type="password"
                            placeholder="Фамилия"
                            id="password"
                            style={{ color: mode === "light" ? "#fff" : "#000"}}
                        />
                    </label>
                    <label htmlFor="password" style={{ color: mode === "light" ? "#fff" : "#000" }}>
                        Пароль
                        <input
                            type="password"
                            placeholder="Номер зачетной книжки или пароль"
                            id="password"
                            style={{ color: mode === "light" ? "#fff" : "#000" }}
                        />
                    </label>
                    <button type="submit" className="submitForm">Войти</button>
                </form>
            </div>
            
            {/* <form name="login_form" className="login_form">
                <h1 style={{color: mode === "light" ? "#FFF" : "#000"}}>Войдите в свой аккаунт</h1>
                <label style={{color: mode === "light" ? "#FFF" : "#000"}}>Имя</label>
                <input name="name" type="text" required/>
                <label style={{color: mode === "light" ? "#FFF" : "#000"}}>Фамилия</label>
                <input name="surname" type="text" required/>
                <label style={{color: mode === "light" ? "#FFF" : "#000"}}>Номер зачетной книжки</label>
                <input name="id" type="text" required/>
                <button className="choose_role">Преподаватель</button>
                <button className="login_btn">Войти</button>
            </form> */}
        </div>
    );
}
