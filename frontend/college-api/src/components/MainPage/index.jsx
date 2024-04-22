import "./style.css";
import { Header } from "./../Header";
import Slider from "./Slider";

function MainPage() {
    return (
        <div className="main">
            <Header />
            <div className="news">
                <div className="line f"></div>
                <Slider />
                <div className="line s"></div>
                <p> Колледж ДГУ - это структурное подразделение Дагестанского государственного университета, 
                    обеспечивающее высокое качество подготовки специалистов среднего звена для удовлетворения потребностей общества в области права, 
                    охраны окружающей среды и природользования, действующее на основании лицензии университета на право ведения образовательной деятельности.
                </p>
            </div>
        </div>
    );
}

export default MainPage;
