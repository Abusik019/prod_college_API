import styles from "./style.module.css";
import axios from "axios";
import { useEffect, useState } from "react";
import getCookie from './../GetCookie/index';

export const AboutDisciplines = () => {
    const [btnBgF, setbtnBgF] = useState("focus");
    const [btnBgS, setbtnBgS] = useState("nofocus");
    const [disciplines, setDisciplines] = useState([]);
    const [myDisciplines, setMyDisciplines] = useState([]);
    const [showDisciplines, setShowDisciplines] = useState(true);
    const [showMyDisciplines, setShowMyDisciplines] = useState(false);
    const [teacherID, setTeacherID] = useState("");
    const accessToken = getCookie("accessToken");
    const headers = {
        Authorization: `Bearer ${accessToken}`,
        "Content-Type": "application/json",
    };

    useEffect(() => {
        const fetchData = async () => {
            try {
                const disciplinesResponse = await axios.get(
                    "http://127.0.0.1:8000/api/v1/data/get_subjects",
                    { headers }
                );
                setDisciplines(disciplinesResponse.data);

                const userResponse = await axios.get(
                    "http://127.0.0.1:8000/api/v1/users/current_user",
                    { headers }
                );
                setMyDisciplines(userResponse.data.subjects)
                setTeacherID(userResponse.data.id);

            } catch (error) {
                console.error("Ошибка при получении данных:", error);
            }
        };

        fetchData();
    }, []);

    useEffect(() => {
        const myDisciplinesByID = new Set(myDisciplines.map((discipline) => discipline.id));
        const updatedDisciplines = disciplines.filter(
            (discipline) => !myDisciplinesByID.has(discipline.id)
        );
        setDisciplines(updatedDisciplines);
    }, [myDisciplines]);

    const addInMyDisciplines = async (groupID) => {
        const myDisciplinesByID = myDisciplines.map((discipline) => discipline.id);

        await axios
            .put(
                `http://127.0.0.1:8000/api/v1/users/teacher_update/${teacherID}`,
                { group_ids: [...myGroupsByID, groupID] },
                { headers }
            )
            .then(() => {
                const newGroup = groups.find((group) => group.id === groupID);
                const updatedMyGroups = [...myGroups, newGroup];
                setMyGroups(updatedMyGroups);

                const updatedGroups = groups.filter(
                    (group) => group.id !== groupID
                );
                setGroups(updatedGroups);
            })
            .catch((error) => {
                console.error(
                    "Ошибка при добавлении группы преподавателя:",
                    error
                );
            });
    };

    // const deleteFromMyGroups = async (groupID) => {
    //     const updatedMyGroups = myGroups.filter(
    //         (group) => group.id !== groupID
    //     );
    //     const updatedMyGroupsByID = updatedMyGroups.map((group) => group.id);

    //     await axios
    //         .put(
    //             `http://127.0.0.1:8000/api/v1/users/teacher_update/${teacherID}`,
    //             { group_ids: updatedMyGroupsByID },
    //             { headers }
    //         )
    //         .then(() => {
    //             const removedGroup = myGroups.find(
    //                 (group) => group.id === groupID
    //             );
    //             const newGroups = [...groups, removedGroup];
    //             setGroups(newGroups);

    //             setMyGroups(updatedMyGroups);
    //         })
    //         .catch((error) => {
    //             console.error(
    //                 "Ошибка при удалении группы преподавателя:",
    //                 error
    //             );
    //         });
    // };

    return (
        <div className={styles.aboutDisciplines}>
            {/* <div className="groups_header">
                <div className="groups-hd_choice">
                    <button
                        style={{
                            backgroundColor:
                                btnBgF === "focus" ? "#A7A7A7" : "#DFDFDF",
                        }}
                        onClick={() => {
                            setbtnBgS("nofocus");
                            setbtnBgF("focus");
                            setShowMyGroups(false);
                            setShowGroups(true);
                        }}
                    >
                        Все специальности
                    </button>
                    <button
                        style={{
                            backgroundColor:
                                btnBgS === "focus" ? "#A7A7A7" : "#DFDFDF",
                        }}
                        onClick={() => {
                            setbtnBgF("nofocus");
                            setbtnBgS("focus");
                            setShowGroups(false);
                            setShowMyGroups(true);
                        }}
                    >
                        Мои специальности
                    </button>
                </div>
            </div>
            <ul
                className="groups_main_content"
                style={{ display: showGroups ? "flex" : "none" }}
            >
                {sortedGroups.map((group) => (
                    <li key={group.id}>
                        <button
                            onClick={() => {
                                addInMyGroups(group.id);
                            }}
                        >
                            +
                        </button>
                        <h1>{group.facult_name}</h1>
                        <h2>{group.course_name} курс</h2>
                        <h3>{group.podgroup_name} группа</h3>
                    </li>
                ))}
            </ul>
            <ul
                className="my_groups_main_content"
                style={{ display: showMyGroups ? "flex" : "none" }}
            >
                {sortedMyGroups.map((group) => (
                    <li key={group.id}>
                        <button
                            onClick={() => {
                                deleteFromMyGroups(group.id);
                            }}
                        >
                            -
                        </button>
                        <h1>{group.facult_name}</h1>
                        <h2>{group.course_name} курс</h2>
                        <h3>{group.podgroup_name} группа</h3>
                    </li>
                ))}
            </ul> */}
        </div>
    );
};
