import "./style.css";
import backBtn from "../../../../assets/back_btn.png";
import readBtn from "../../../../assets/read.png";
import { useEffect, useState } from "react";
import { AboutTeachers } from '../../../AboutTeachers';
import { Link } from 'react-router-dom';

const data = [
    {
      'name': 'Название лекции',
      'date': '25.05.2020'  
    },
    {
      'name': 'Название лекции',
      'date': '25.05.2020'  
    },
    {
      'name': 'Название лекции',
      'date': '25.05.2020'  
    },
    {
      'name': 'Название лекции',
      'date': '25.05.2020'  
    },
    {
      'name': 'Название лекции',
      'date': '25.05.2020'  
    },
    {
      'name': 'Название лекции',
      'date': '25.05.2020'  
    },
]

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
                    {data.map((item, index) => (
                        <li key={index}>
                            <div className="l-list_text_cont">
                                <h1>{item.name}</h1>
                                <h2>{item.date}</h2>
                            </div>
                            <Link to="/lecture"><button><img src={readBtn}/></button></Link>
                        </li>
                    ))} 
                </ul>
            </div>
            {back && <AboutTeachers />}
        </>
    );

};
