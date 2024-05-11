import "./style.css";
import list from "../../../assets/list.png";

export const AboutTeacher = ({image, name, subject, handleTeacherLectures, }) => {
    return (
        <li className="teachers_container_child">
            <img src={image} />
            <div className="tc-text">
                <h1>{name}</h1>
                <h2>{subject}</h2>
            </div>
            <button onClick={handleTeacherLectures}><img src={list}/></button>
        </li>
    );
};
