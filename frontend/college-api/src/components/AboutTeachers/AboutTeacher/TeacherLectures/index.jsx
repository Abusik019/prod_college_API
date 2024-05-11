import "./style.css";
import backBtn from "../../../../assets/back_btn.png";
import { useEffect, useState } from "react";
import { AboutTeachers } from '../../../AboutTeachers';

export const TeacherLectures = () => {
    const [back, setBack] = useState(false);
    const [isOverflowing, setIsOverflowing] = useState(false);

    useEffect(() => {
        const list = document.querySelector(".l-list_btm_side");
        if (list && list.childNodes.length > 3) {
            setIsOverflowing(true);
        } else {
            setIsOverflowing(false);
        }
    }, []);


    return (
        <>
            <div className="lectures_list" style={{display: back ? 'none' : 'block'}}>
                <div className="l-list_top_side">
                    <button onClick={() => setBack(true)}>
                        <img src={backBtn}/>
                    </button>
                    <div className="l-list_text">
                        <h1>Имя отчество</h1>
                        <h2>предмет</h2>
                    </div>
                </div>
                <div className="l-list_line"></div>
                <ul className="l-list_btm_side"  style={{ overflowY: isOverflowing ? "scroll" : "auto"}}>
                    <li>
                        <h1>Название лекции</h1>
                        <button>Читать</button>
                    </li>
                    <li>
                        <h1>Название лекции</h1>
                        <button>Читать</button>
                    </li>
                    <li>
                        <h1>Название лекции</h1>
                        <button>Читать</button>
                    </li>
                    <li>
                        <h1>Название лекции</h1>
                        <button>Читать</button>
                    </li>
                    <li>
                        <h1>Название лекции</h1>
                        <button>Читать</button>
                    </li>
                </ul>
            </div>
            {back && <AboutTeachers />}
        </>
    );

};
