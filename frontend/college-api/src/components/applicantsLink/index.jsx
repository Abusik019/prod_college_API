import "./style.css";
import { useContext } from "react";
import { ThemeContext } from "../themeContext";

export const ApplicantsLink = ({ link, text }) => {
    const { mode } = useContext(ThemeContext);

    return (
        <a href={link} className="applicants_link" style={{color: mode === "light" ? '#fff' : '#000'}}>
            {text}
        </a>
    );
};
