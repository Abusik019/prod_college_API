import { useContext } from "react";
import "./style.css"
import { ThemeContext } from "../themeContext";

export const Footer = () => {
  const { mode } = useContext(ThemeContext);

  return (
    <>
      <div className="line s" style={{background: mode === "light" ? "#FF7A00" : "#000"}}></div>
      <div className="main_footer">
        <p>Колледж ДГУ © 2024 Дагестанский государственный университет 367000, г.Махачкала, ул.Дзержинского, 21, тел: (8-722) 67-23-27 Разработка и поддержка сайта: +7(989) 678-91-20, +7(903) 429-40-70</p>
      </div>
    </>
  )
}
