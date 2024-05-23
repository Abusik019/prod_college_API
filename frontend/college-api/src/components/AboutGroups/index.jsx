import "./style.css";
import axios from "axios";
import { useEffect, useState, useCallback } from "react";
import getCookie from './../GetCookie/index';
import { ChooseSortGroups } from './../ChooseSortGroups/index';

export const AboutGroups = () => {
    const [btnBgF, setbtnBgF] = useState('focus');
    const [btnBgS, setbtnBgS] = useState('nofocus');
    const [groups, setGroups] = useState([]);
    const [myGroups, setMyGroups] = useState([]);
    const [isOverflowing, setIsOverflowing] = useState(false);
    const [showGroups, setShowGroups] = useState(true);
    const [showMyGroups, setShowMyGroups] = useState(false);
    const [teacherID, setTeacherID] = useState('');
    const accessToken = getCookie("accessToken");
    const [sortBy, setSortBy] = useState([]);
    const headers = {
        'Authorization': `Bearer ${accessToken}`,
        'Content-Type': 'application/json'
    };

    useEffect(() => {
        const fetchData = async () => {
            try {
                const groupsResponse = await axios.get("http://127.0.0.1:8000/api/v1/data/get_groups", { headers });
                const sortedGroups = groupsResponse.data.sort((a, b) => a.facult_name.localeCompare(b.facult_name));
                setGroups(sortedGroups);

                const myGroupsResponse = await axios.get("http://127.0.0.1:8000/api/v1/users/my_groups", { headers });
                const sortedMyGroups = myGroupsResponse.data.sort((a, b) => a.facult_name.localeCompare(b.facult_name));
                setMyGroups(sortedMyGroups);

                const userResponse = await axios.get("http://127.0.0.1:8000/api/v1/users/current_user", { headers });
                setTeacherID(userResponse.data.id);
                
            } catch (error) {
                console.error('Ошибка при получении данных:', error);
            }
        };

        fetchData();
    }, []);

    useEffect(() => {
        const myGroupsByID = new Set(myGroups.map(group => group.id));
        const updatedGroups = groups.filter(group => !myGroupsByID.has(group.id));
        setGroups(updatedGroups);
    }, [myGroups]);

    const addInMyGroups = async (groupID) => {
        const myGroupsByID = myGroups.map(group => group.id);

        await axios.put(`http://127.0.0.1:8000/api/v1/users/teacher_update/${teacherID}`, { "group_ids": [...myGroupsByID, groupID]}, { headers })
            .then(() => {
                const newGroup = groups.find(group => group.id === groupID);
                const updatedMyGroups = [...myGroups, newGroup];
                setMyGroups(updatedMyGroups);

                const updatedGroups = groups.filter(group => group.id !== groupID);
                setGroups(updatedGroups);
            })
            .catch((error) => {
                console.error('Ошибка при добавлении группы преподавателя:', error);
            });
    };

    const deleteFromMyGroups = async (groupID) => {
        const updatedMyGroups = myGroups.filter(group => group.id !== groupID);
        const updatedMyGroupsByID = updatedMyGroups.map(group => group.id);
    
        await axios.put(`http://127.0.0.1:8000/api/v1/users/teacher_update/${teacherID}`, { "group_ids": updatedMyGroupsByID }, { headers })
            .then(() => {
                const removedGroup = myGroups.find(group => group.id === groupID);
                const newGroups = [...groups, removedGroup];
                setGroups(newGroups.sort((a, b) => a.facult_name.localeCompare(b.facult_name)));
    
                setMyGroups(updatedMyGroups);
            })
            .catch((error) => {
                console.error('Ошибка при удалении группы преподавателя:', error);
            });
    };
    

    const getSortInfo = useCallback((sortOption) => {
        setSortBy(sortOption);
    }, []);

    return (
        <div className="groups">
            <div className="groups_header">
                <div className="groups-hd_choice">
                    <button 
                        style={{backgroundColor: btnBgF === 'focus' ? '#A7A7A7' : '#DFDFDF' }}
                        onClick={() => {
                            setbtnBgS('nofocus');
                            setbtnBgF('focus');
                            setShowMyGroups(false);
                            setShowGroups(true);
                        }}
                    >Все группы</button>
                    <button 
                        style={{backgroundColor: btnBgS === 'focus' ? '#A7A7A7' : '#DFDFDF' }}
                        onClick={() => {
                            setbtnBgF('nofocus');
                            setbtnBgS('focus');
                            setShowGroups(false);
                            setShowMyGroups(true);
                        }}
                    >Мои группы</button>
                </div>
                <button className="change_group"
                    onClick={() => {
                        const item = document.querySelector('.choose_sort');
                        item.classList.add('active');
                    }}
                >Сортировать</button>
                <div className="choose_sort">
                    <button className="hide_checkbox" 
                        onClick={() => {
                            const item = document.querySelector('.choose_sort');
                            item.classList.remove('active');
                        }}
                    >&#10006;</button>
                    <ChooseSortGroups getSortInfo={getSortInfo}/>
                </div>
            </div>
            <ul className="groups_main_content" style={{ overflowY: isOverflowing ? "scroll" : "auto", display: showGroups ? 'flex' : 'none'}}>
                {groups.map(group => (
                    <li key={group.id}>
                        <button
                             onClick={() => {
                                addInMyGroups(group.id);
                            }}
                        >+</button>
                        <h1>{group.facult_name}</h1>
                        <h2>{group.course_name} курс</h2>
                        <h3>{group.podgroup_name} группа</h3>
                    </li>
                ))}
            </ul>
            <ul className="my_groups_main_content" style={{ overflowY: isOverflowing ? "scroll" : "auto", display: showMyGroups ? 'flex' : 'none'}}>
                {myGroups.map(group => (
                    <li key={group.id}>
                        <button
                            onClick={() => {
                                deleteFromMyGroups(group.id)
                            }}
                        >-</button>
                        <h1>{group.facult_name}</h1>
                        <h2>{group.course_name} курс</h2>
                        <h3>{group.podgroup_name} группа</h3>
                    </li>
                ))}
            </ul>
        </div>
    );
};
