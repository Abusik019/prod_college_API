import { useState } from "react";
import "./style.css";
import { AboutTeachers } from '../../../AboutTeachers';

export const TeacherLectures = () => {
    const [back, setBack] = useState(false);

    return (
        <>
            <div className="lectures_list" style={{display: back ? 'none' : 'block'}}>
                <h1>Список лекций</h1>
                <button onClick={() => 
                    setBack(true)
                }>Назад</button>
            </div>
            {back && <AboutTeachers />}
        </>
    );

};
