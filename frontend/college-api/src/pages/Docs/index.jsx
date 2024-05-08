import "./style.css";
import { Header } from "./../../components/Header/index";
import { LiDocs } from "./../../components/LIDocs/index";
import { Footer } from "./../../components/Footer/index";
import { useContext } from "react";
import { ThemeContext } from "../../components/themeContext";

function Documents() {
        const { mode } = useContext(ThemeContext);

    return (
        <div className="documents" style={{backgroundColor: mode === "light" ? '#313131' : '#E7E7E7'}}>
            <Header />
            <div className="docs_content">
                <h1 style={{color: mode === "light" ? '#fff' : '#000'}}>Документы Колледжа ДГУ</h1>
                <ul className="docs_links">
                    <LiDocs
                        link="https://ndoc.dgu.ru/PDFF/Polojenie_GIA_SPO_2024.pdf"
                        text='"Положение о проведении государственной итоговой аттестации по образовательным программам среднего профессионального образования в Дагестанском государственном университете"'
                        date="2024.03.04"
                    />
                    <LiDocs
                        link="https://ndoc.dgu.ru/PDFF/Pologenie_o_por_zap_i_vid_doc_ob_obraz_SPO_2023.pdf"
                        text='"Положение о порядке заполнения, учета и выдачи документов о среднем профессиональном образовании, приложений к ним и их дубликатов в Дагестанском государственном университете"'
                        date="2023.06.05"
                    />
                    <LiDocs
                        link="https://ndoc.dgu.ru/PDFF/Polojenie_o_perehode_s_PO_na_BO_SPO_2023.pdf"
                        text='"Положение о порядке и случаях перехода лиц, обучающихся по образовательным программам среднего профессионального и высшего образования, с платного обучения на бесплатное в Дагестанском государственном университете"'
                        date="2023.04.17"
                    />
                    <LiDocs
                        link="https://ndoc.dgu.ru/PDFF/Polojenie_ob_organiz_sam_rab_obuch_SPO_DGU.pdf"
                        text='"Положение об организации самостоятельной работы обучающихся, осваивающих программы среднего профессионального образования в колледже Дагестанского государственного университета"'
                        date="2015"
                    />
                    <LiDocs
                        link="https://ndoc.dgu.ru/PDFF/1536.pdf"
                        text='"Положение о колледже ФГБОУ ВО «Дагестанский государственный университет»"'
                        date="2022"
                    />
                    <LiDocs
                        link="https://ndoc.dgu.ru/PDFF/Polojenie_o_por_zap_uch_i_vid_svid_2022.pdf"
                        text='"Положение о порядке заполнения, учета и выдачи свидетельств о профессии рабочего, должности служащего обучающимся, осваивающим образовательные программы среднего профессионального образования в Дагестанском государственном университете"'
                        date="2022.05.06"
                    />
                    <LiDocs
                        link="https://ndoc.dgu.ru/PDFF/Polog_ob_individ_and_uskor_obuch_SPO_2022.pdf"
                        text='"Положение о порядке обучения студентов по индивидуальному плану, ускоренному обучению по образовательным программам среднего профессионального образования в Дагестанском государственном университете"'
                        date="2022.04.22"
                    />
                    <LiDocs
                        link="https://ndoc.dgu.ru/PDFF/Pologenie_o_kontr_uspev_obuch_UK_2022.pdf"
                        text='"Положение об организации и проведении текущего контроля успеваемости и промежуточной аттестации обучающихся по основным образовательным программам среднего профессионального образования в Дагестанском государственном университете"'
                        date="2022.04.22"
                    />
                    <LiDocs
                        link="https://ndoc.dgu.ru/PDFF/Polojenie_GIA_SPO_2022.pdf"
                        text='"Положение о проведении государственной итоговой аттестации по образовательным программам среднего профессионального образования в Дагестанском государственном университете"'
                        date="2022"
                    />
                    <LiDocs
                        link="https://ndoc.dgu.ru/PDFF/Poloj_o_FOS_Law_Coll_2015.pdf"
                        text='"Положение о формировании фонда оценочных средств для проведения текущего контроля успеваемости и промежуточной аттестации обучающихся по программам среднего профессионального образования в Дагестанском государственном университете"'
                        date="2015"
                    />
                    <LiDocs
                        link="https://ndoc.dgu.ru/PDFF/Poloj_o_praktik_SPO_2019.pdf"
                        text='"ПОЛОЖЕНИЕ о практике обучающихся, осваивающих основные профессиональные образовательные программы среднего профессионального образования в Дагестанском государственном университете"'
                        date="2019.01.31"
                    />
                    <LiDocs
                        link="https://ndoc.dgu.ru/PDFF/Poloj_kursov_rab_SPO_2018.pdf"
                        text='"Положение о курсовых работах (проектах), выполняемых обучающимися при освоении программ среднего профессионального образования в Дагестанском государственном университете"'
                        date="2019.01.31"
                    />
                    <LiDocs
                        link="https://ndoc.dgu.ru/PDFF/Pologenie_o_zachete_UK2016.pdf"
                        text='"Положение о зачете"'
                        date="2016"
                    />
                    <LiDocs
                        link="https://ndoc.dgu.ru/PDFF/Pologenie_o_proved_KE_PM_SPO_2018.pdf"
                        text='"Положение о проведении квалификационного экзамена по профессиональному модулю (профессиональным модулям) по образовательным программам среднего профессионального образования в Дагестанском государственном университете"'
                        date="2018.04.10"
                    />
                    <LiDocs
                        link="https://ndoc.dgu.ru/PDFF/Pologenie_o_rejime_zan_UK2016.pdf"
                        text='"Положение о режиме занятий обучающихся"'
                        date="2016"
                    />
                </ul>
            </div>
            <Footer />
        </div>
    );
}

export default Documents;
