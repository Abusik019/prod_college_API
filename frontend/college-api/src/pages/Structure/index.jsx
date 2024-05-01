import "./style.css";
import { Header } from './../../components/Header/index';
import { Footer } from './../../components/Footer/index';
import { ThemeContext } from './../../components/themeContext/index';
import { useContext } from "react";

function Structure() {
    const { mode } = useContext(ThemeContext);
    const isLight = {color: mode === 'light' ? '#fff': '#000'}

    return <div className="structure" style={{backgroundColor: mode === 'light' ? '#313131': '#E7E7E7'}}>
        <Header />
        <table>
            <tr> 
                <th style={isLight}>Подразделения</th>
                <th style={isLight}>Руководители подразделения</th>
                <th style={isLight}>Контакты</th>
            </tr>
            <tr>
                <td style={isLight}>Администрация</td>
                <td style={isLight}>Пирбудагова Диана Шамильевна <br /><span>Директор колледжа ДГУ</span></td>
                <td style={isLight}>67-17-52<br />Email: pirbudagovad@mail.ru</td>
            </tr>
            <tr>
                <td style={isLight}>Учебная часть</td>
                <td style={isLight}>Иразиханова Наринжа Салимовна<br /><span>зам.директора по учебной работе;</span><br />
                    <br />
                    Галимов Сагид Абдулгалимович<br /><span>зам.директора по воспитательной работе;</span><br />
                    <br />
                    Мусалова Заира Магомедовна<br /><span>зам.директора по опережающему профессиональному развитию;</span><br />
                    <br />
                    Габиева Сиясат Магомедовна<br /><span>зав.отделением по специальности 40.02.01 «Право и организация социального обеспечения»;</span><br />
                    <br />
                    Исаева Карина Мустангировна<br /><span>зав.отделением по специальности 40.02.02 «Правоохранительная деятельность»;</span><br />
                    <br />
                    Камилова Джума Валиевна<br /><span>зав. отделением по специальности 40.02.03 "Право и судебное администрирование";</span><br />
                    <br />
                    Курбанова Наида Сеферуллаевна<br /><span>зав. отделением по специальности 20.02.01 «Рациональное использование природохозяйственных комплексов»;</span><br />
                    <br />
                    Абдуллаева Наргис Ассадуллаевна<br /><span>зав. отделением по специальности «Информационные системы и программирование»;</span><br />
                    <br />
                    Магдилова Лариса Владимировна<br /><span>зав. отделением по специальности «Обеспечение информационной безопасности автоматизированных систем»;</span><br />
                    <br />
                    Дидиченко Елена Шукуровна<br /><span>ст. методист по специальности "Право и организация социального обеспечения";</span><br />
                    <br />
                    Шамсутдинова Умжат Алиевна<br /><span>ст. методист по специальности "Правоохранительная деятельность";</span><br />
                    <br />
                    Магомедова Аида Абасовна<br /><span>ст. методист по специальности "Право и судебное администрирование";</span><br />
                    <br />
                    Изиева Зарема Алиевна<br /><span>ст. методист по специальности "Рациональное использование природохозяйственных комплексов";</span><br />
                    <br />
                    Далгатова Зарина Ибрагимовна<br /><span>ст.методист по специальности «Информационные системы и программирование»;</span><br />
                    <br />
                    Шамсутдинова Ума Абдулмаликовна<br /><span>ст.методист по специальности «Обеспечение информационной безопасности автоматизированных систем»</span></td>
                <td style={isLight}>67-42-65 collegedsu@mail.ru</td>
            </tr>
        </table>
        <h1 className="department" style={{color: mode === 'light' ? '#fff': '#000'}}>Кафедры</h1>
        <table className="secondTable">
            <tr> 
                <th style={isLight}>Наименования</th>
                <th style={isLight}>Руководители</th>
                <th style={isLight}>Контакты</th>
            </tr>
            <tr>
                <td style={isLight}>Кафедра естественнонаучных и гуманитарных дисциплин</td>
                <td style={isLight}><span>Зав. кафедрой</span><br/>Муртилова Камила Магомед-Камильевна<br/><br/><span>ст. лаборант</span><br/>Айдемирова Асият Шамхаловна</td>
                <td style={isLight}>67-32-08<br/>E-mail: kaf_edg2018@mail.ru</td>
            </tr>
            <tr>
                <td style={isLight}>Кафедра общепрофессиональных дисциплин</td>
                <td style={isLight}><span>Зав. кафедрой</span><br/>Магомедова Патимат Расуловна<br/><br/><span>ст. лаборант</span><br/>Гасанбекова Зейнаб Аликеримовна</td>
                <td style={isLight}>56-21-80<br/>E-mail: kafedraopd_jurcolledge@mail.ru</td>
            </tr>
            <tr>
                <td style={isLight}>Базовая кафедра специальных дисциплин</td>
                <td style={isLight}><span>Зав. кафедрой</span><br/>Магомедова Карина Камильевна<br/><br/><span>ст. лаборант</span><br/>Курбанова Патимат Магомедовна</td>
                <td style={isLight}>56-21-81<br/>98-49-22<br/>98-49-29<br/>kafedra_sd@mail.ru</td>
            </tr>
            <tr>
                <td style={isLight}>Базовая кафедра специальных дисциплин</td>
                <td style={isLight}><span>Зав. кафедрой</span><br/>Магомедова Карина Камильевна<br/><br/><span>ст. лаборант</span><br/>Курбанова Патимат Магомедовна</td>
                <td style={isLight}>56-21-81<br/>akvila69@mail.ru</td>
            </tr>
            <tr>
                <td style={isLight}>Медицинская сестра</td>
                <td style={isLight}>Шамсудинова Диляра Магомедовна</td>
                <td style={isLight}>67-42-65<br/>collegedsu@mail.ru</td>
            </tr>
            <tr>
                <td style={isLight}>Зав. кабинетами</td>
                <td style={isLight}>Шабанова Нурия Нуруллаховна,<br/><br/>Гитинова Айзанат Магомедовна</td>
                <td style={isLight}>67-42-65<br/>shabanova_nuriya@mail.ru<br/>ventido05@mail.ru</td>
            </tr>
            <tr>
                <td style={isLight}>Документовед</td>
                <td style={isLight}>Яхьяева Меседу Исмаиловна</td>
                <td style={isLight}>56-21-61</td>
            </tr>
        </table>
        <Footer />
    </div>;
}

export default Structure;
