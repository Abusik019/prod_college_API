import { useContext } from "react";
import "./style.css";
import { ThemeContext } from "../themeContext";

export const LiDocs = ({ link, text, date }) => {
    const { mode } = useContext(ThemeContext);

    return (
        <li className="li_docs">
            <a href={link} style={{color: mode === "light" ? '#fff' : '#000'}}>{text}</a>
            <h1>{date}</h1>
        </li>
    );
};
