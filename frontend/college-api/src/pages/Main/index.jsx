import "./style.css";
import { Header } from './../../components/Header';
import { Faculty } from "../../components/Faculty";
import Slider from "../../components/Slider";
import { useContext } from "react";
import { ThemeContext } from "../../components/themeContext";
import { Footer } from './../../components/Footer';

function Main() {
    const { mode } = useContext(ThemeContext);

    return (
        <div className="main" style={{background: mode === "light"  ? "#313131" : "#E7E7E7"}}>
            <Header />
            <div className="news">
                <div className="line f" style={{background: mode === "light" ? "#FF7A00" : "#000"}}></div>
                <Slider />
                <div className="line s" style={{background: mode === "light" ? "#FF7A00" : "#000"}}></div>
                <p style={{color: mode === "light" ? "#FFF" : "#000"}}> Колледж ДГУ - это структурное подразделение Дагестанского государственного университета, 
                    обеспечивающее высокое качество подготовки специалистов среднего звена для удовлетворения потребностей общества в области права, 
                    охраны окружающей среды и природользования, действующее на основании лицензии университета на право ведения образовательной деятельности.
                </p>
            </div>
            <div className="faculties">
                <Faculty description='09.02.07 "Информационные системы и программирование"' imagePath="../../../../src/assets/isip.jfif" />
                <Faculty description='10.05.02 "Обеспечение информационной безопасности автоматизированных систем"' imagePath="../../../../src/assets/oebas.jfif" />
                <Faculty description='40.02.01 Право и организация социального обеспечения' imagePath="../../../../src/assets/pso.jfif" />
                <Faculty description='40.02.03 Право и судебное администрирование' imagePath="../../../../src/assets/psa.jpg" />
                <Faculty description='40.02.02 Правоохранительная деятельность' imagePath="../../../../src/assets/pd.jfif" />
                <Faculty description='20.02.01 Экологическая безопасность природных комплексов' imagePath="../../../../src/assets/ripk.jfif" />
            </div>
            <div className="line t" style={{background: mode === "light" ? "#FF7A00" : "#000"}}></div>
            <div className="pressed_links">
                <a href="https://dgu.ru/Abitur/Files/priem2024/normdoc/podacha_doc.pdf" style={{color: mode === "light" ? "#FFF" : "#000"}}>Информация о способах подачи документов</a>
                <a href="https://dgu.ru/Abitur/Files/priem2024/normdoc/pocht_add.pdf" style={{color: mode === "light" ? "#FFF" : "#000"}}>Информация о почтовых адресах для направления документов, необходимых для поступления</a>
                <a href="https://dgu.ru/Abitur/Files/priem2024/normdoc/VI_ovz.pdf" style={{color: mode === "light" ? "#FFF" : "#000"}}>Особенности проведения ВИ для лиц с ОВЗ и инвалидов</a>
            </div>
            <Footer />
        </div>
    );
}

export default Main;