import axios from "axios";
import "./style.css";
import { Link, useNavigate } from "react-router-dom";
import { useContext, useEffect, useState } from "react";
import { ThemeContext } from "../../components/themeContext";
import { ToggleThemeBtn } from "../../components/ToggleThemeBtn";
import getCookie from "./../../components/GetCookie/index.js";
import darkLogo from "../../assets/logo.png";
import lightLogo from "../../assets/light-logo.png";
import darkUser from "../../assets/darkuser.png";
import lightUser from "../../assets/lightuser.png";

export default function Login() {
    const navigate = useNavigate();
    const { mode } = useContext(ThemeContext);
    const [username, setUsername] = useState("");
    const [userSurname, setUserSurname] = useState("");
    const [userPassword, setUserPassword] = useState("");
    const [accessToken, setAccessToken] = useState(getCookie("accessToken"));
    const headers = {
        Authorization: `Bearer ${accessToken}`,
        "Content-Type": "application/json",
    };

    useEffect(() => {
        if (accessToken) {
            checkUserRole();
        }
    }, [accessToken]);

    function checkUserRole() {
        axios.get("http://127.0.0.1:8000/api/v1/users/current_user", { headers })
            .then((response) => {
                console.log(response);
                if (response.data.is_teacher) {
                    navigate("/teacher-profile");
                } else {
                    navigate("/profile");
                }
            })
            .catch((error) => {
                console.log(error);
            });
    }

    function sendUserData(e) {
        e.preventDefault();
        
        const requestData = {
            first_name: username,
            last_name: userSurname,
            college_id: userPassword,
        };

        axios.post('http://127.0.0.1:8000/api/token/', requestData)
            .then((response) => {   
                if (response.status === 200) {
                    document.cookie = `accessToken=${response.data.access}`;
                    setAccessToken(response.data.access);
                }
            })
            .catch((error) => {
                console.log(error);
            });
    }

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
                    <div className="imageWrapper">
                        <img src={mode === "light" ? lightUser : darkUser} />
                    </div>
                    <label
                        htmlFor="username"
                        style={{ color: mode === "light" ? "#fff" : "#000" }}
                    >
                        Имя
                        <input
                            type="text"
                            placeholder="Имя"
                            id="username"
                            style={{
                                color: mode === "light" ? "#fff" : "#000",
                            }}
                            onChange={(e) => {
                                setUsername(e.target.value);
                            }}
                        />
                    </label>
                    <label
                        htmlFor="surname"
                        style={{ color: mode === "light" ? "#fff" : "#000" }}
                    >
                        Фамилия
                        <input
                            type="text"
                            placeholder="Фамилия"
                            id="surname"
                            style={{
                                color: mode === "light" ? "#fff" : "#000",
                            }}
                            onChange={(e) => {
                                setUserSurname(e.target.value);
                            }}
                        />
                    </label>
                    <label
                        htmlFor="password"
                        style={{ color: mode === "light" ? "#fff" : "#000" }}
                    >
                        Пароль
                        <input
                            type="password"
                            placeholder="Номер зачетной книжки или пароль"
                            id="password"
                            style={{
                                color: mode === "light" ? "#fff" : "#000",
                            }}
                            onChange={(e) => {
                                setUserPassword(e.target.value);
                            }}
                        />
                    </label>
                    <button
                        type="submit"
                        className="submitForm"
                        onClick={sendUserData}
                    >
                        Войти
                    </button>
                </form>
            </div>
        </div>
    );
}
