import { useContext } from "react";
import "./style.css";
import dark from "../../assets/dark.png";
import light from "../../assets/light.png";
import { ThemeContext } from '../themeContext';

export const ToggleThemeBtn = ({left = 0, top = 0, right = 0, bottom = 0}) => {
    const { mode, toggleMode } = useContext(ThemeContext);

    return (
        <button 
            className="toggle_theme_btn" 
            style={{right: right, top: top, left: left, bottom: bottom}}
            onClick={() => {toggleMode(mode === "dark" ? "light" : "dark")}}
        >
            <img src={mode === "dark" ? dark : light}/>
        </button>
    )
}
