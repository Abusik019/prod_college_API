import "./style.css";
import { useContext } from "react";
import { ThemeContext } from './../../components/themeContext';
import { Header } from './../../components/Header';

function Lecture() {
    const { mode } = useContext(ThemeContext);

    return (
        <div className="lecture" style={{ background: mode === "light" ? "#313131" : "#E7E7E7" }}>
            <Header />
        </div>
    );
}

export default Lecture;
