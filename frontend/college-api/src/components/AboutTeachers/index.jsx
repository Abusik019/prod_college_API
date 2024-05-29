import "./style.css";
import { useState } from "react";
import { AboutTeacher } from "./AboutTeacher";
import { TeacherLectures } from "./AboutTeacher/TeacherLectures";

export const AboutTeachers = () => {
    const [teacherLectures, setTeacherLectures] = useState(false);

    function handleTeacherLectures() {
        setTeacherLectures(true);
    }

    return (
        <>
            <ul
                className="teachers_container"
                style={{ display: teacherLectures ? 'none' : 'flex'}}
            >
                <AboutTeacher
                    image="https://img.championat.com/c/900x900/news/big/x/t/kak-margo-robbi-svyazana-s-figurkoj_16908998241368568729.jpg"
                    name="Имя Отчество"
                    subject="предмет"
                    handleTeacherLectures={handleTeacherLectures}
                />
                <AboutTeacher
                    image="https://img.championat.com/c/900x900/news/big/x/t/kak-margo-robbi-svyazana-s-figurkoj_16908998241368568729.jpg"
                    name="Имя Отчество"
                    subject="предмет"
                    handleTeacherLectures={handleTeacherLectures}
                />
                <AboutTeacher
                    image="https://img.championat.com/c/900x900/news/big/x/t/kak-margo-robbi-svyazana-s-figurkoj_16908998241368568729.jpg"
                    name="Имя Отчество"
                    subject="предмет"
                    handleTeacherLectures={handleTeacherLectures}
                />
                <AboutTeacher
                    image="https://img.championat.com/c/900x900/news/big/x/t/kak-margo-robbi-svyazana-s-figurkoj_16908998241368568729.jpg"
                    name="Имя Отчество"
                    subject="предмет"
                    handleTeacherLectures={handleTeacherLectures}
                />
            </ul>
            {teacherLectures && <TeacherLectures />}
        </>
    );
};
