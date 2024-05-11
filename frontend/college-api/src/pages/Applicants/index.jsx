import './style.css';
import { Header } from './../../components/Header';
import { ApplicantsLink } from './../../components/applicantsLink/index';
import { Footer } from './../../components/Footer/index';
import { useContext } from 'react';
import { ThemeContext } from '../../components/themeContext';

function Applicants() {
    const { mode } = useContext(ThemeContext);

  return (
    <div className='applicants' style={{backgroundColor: mode === "light" ? '#313131' : '#E7E7E7'}}>
        <Header />
        <h1 style={{color: mode === "light" ? '#fff' : '#000'}}>Среднее профессиональное образование</h1>
        <div className='line app'></div>
        <div className='applicants_links'>
            <ApplicantsLink link='https://dgu.ru/Abitur/Files/priem2024/normdoc/%D0%9F%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D0%B0%20%D0%BF%D1%80%D0%B8%D0%B5%D0%BC%D0%B0%20%D0%A1%D0%9F%D0%9E%202024.pdf' 
                            text='Правила приема в ФГБОУ ВО "Дагестанский государственный университет" на обучение по образовательным программам среднего профессионального образования в 2024-2025 уч.г. '/>
            <ApplicantsLink link='https://dgu.ru/Abitur/Files/priem2024/normdoc/%D0%9F%D0%B5%D1%80%D0%B5%D1%87%D0%B5%D0%BD%D1%8C%20%D1%81%D0%BF%D0%B5%D1%86%D0%B8%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D1%81%D1%82%D0%B5%D0%B9%20%D0%A1%D0%9F%D0%9E%202024.pdf' 
                            text='Перечень специальностей СПО, по которым ФГБОУ ВО "Дагестанский государственный университет" и его филиалы осуществляют прием в 2024/2025 учебном году'/>
            <ApplicantsLink link='https://dgu.ru/Abitur/Files/priem2024/normdoc/%D0%A2%D1%80%D0%B5%D0%B1%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F%20%D0%BA%20%D1%83%D1%80%D0%BE%D0%B2%D0%BD%D1%8E%20%D0%BE%D0%B1%D1%80%D0%B0%D0%B7%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8F%202024.pdf' 
                            text='Требования к уровню образования, которое необходимо для поступления на образовательные программы СПО в ФГБОУ ВО "Дагестанский государственный университет"'/>
            <ApplicantsLink link='https://dgu.ru/Abitur/Files/priem2024/normdoc/%D0%A3%D1%81%D0%BB%D0%BE%D0%B2%D0%B8%D1%8F%20%D0%BF%D1%80%D0%B8%D0%B5%D0%BC%D0%B0%20%D0%BD%D0%B0%20%D0%9F%D0%9E%20%D0%A1%D0%9F%D0%9E%202024.pdf' 
                            text='Условия приема на обучение по договорам об оказании платных образовательных услуг на образовательные программы СПО в ФГБОУ ВО "Дагестанский государственный университет"'/>
            <ApplicantsLink link='https://dgu.ru/Abitur/Files/priem2024/normdoc/%D0%9F%D0%95%D0%A0%D0%95%D0%A7%D0%95%D0%9D%D0%AC%20%D0%92%D0%98%20%D0%A1%D0%9F%D0%9E%202024.pdf' 
                            text='Перечень и формы вступительных испытаний при приеме на обучение по образовательным программам СПО'/>
            <ApplicantsLink link='https://dgu.ru/Abitur/Files/priem2024/normdoc/%D0%9E%D1%81%D0%BE%D0%B1%D0%B5%D0%BD%D0%BD%D0%BE%D1%81%D1%82%D0%B8%20%D0%92%D0%98%20%D0%B8%D0%BD%D0%B2%D0%B0%D0%BB%D0%B8%D0%B4%D1%8B%202024.pdf' 
                            text='Особенности проведения ВИ для лиц с ОВЗ и инвалидов при приеме на обучение по образовательным программам СПО'/>
            <ApplicantsLink link='https://dgu.ru/Abitur/Files/priem2024/normdoc/%D0%98%D0%BD%D1%84%D0%BE%D1%80%D0%BC%D0%B0%D1%86%D0%B8%D1%8E%20%D0%BE%20%D0%BC%D0%B5%D0%B4%D0%BE%D1%81%D0%BC%D0%BE%D1%82%D1%80%D0%B5%202024.pdf' 
                            text='Информация о необходимости прохождения поступающими на образовательные программы СПО обязательного предварительного медицинского осмотра'/>
            <ApplicantsLink link='https://dgu.ru/Abitur/?id=22789' 
                            text='Контрольные цифры приема'/>
            <ApplicantsLink link='https://dgu.ru/Abitur/?id=22784' 
                            text='Программы вступительных испытаний'/>
        </div>
        <Footer />
    </div>
  )
}

export default Applicants