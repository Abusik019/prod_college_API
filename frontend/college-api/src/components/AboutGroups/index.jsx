import "./style.css";
import axios from "axios";
import { useEffect, useState } from "react";
import getCookie from './../GetCookie/index';

export const AboutGroups = () => {
    const [btnBgF, setbtnBgF] = useState('focus');
    const [btnBgS, setbtnBgS] = useState('nofocus');
    const [groups, setGroups] = useState([]);
    const [isOverflowing, setIsOverflowing] = useState(false);
    const accessToken = getCookie("accessToken");
    const headers = {
        'Authorization': `Bearer ${accessToken}`,
        'Content-Type': 'application/json'
    };

    console.log(groups);

    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/v1/data/get_groups", { headers })
            .then((response) => {
                // console.log(response);
                setGroups(response.data);
            })
            .catch((error) => {
                console.log(error);
            });

        const tc = document.querySelector(".groups_main_content");
            if (tc && tc.childNodes.length > 7) {
                setIsOverflowing(true);
            } else {
                setIsOverflowing(false);
            }
    }, []);

    return (
        <div className="groups">
            <div className="groups_header">
                <div className="groups-hd_choice">
                    <button 
                        style={{backgroundColor: btnBgF === 'focus' ? '#A7A7A7' : '#DFDFDF' }}
                        onClick={() => {
                            setbtnBgS('nofocus')
                            setbtnBgF('focus')
                        }}
                    >Все группы</button>
                    <button 
                        style={{backgroundColor: btnBgS === 'focus' ? '#A7A7A7' : '#DFDFDF' }}
                        onClick={() => {
                            setbtnBgF('nofocus')
                            setbtnBgS('focus')
                        }}
                    >Мои группы</button>
                </div>
                <button className="change_group">Изменить</button>
            </div>
            <ul className="groups_main_content" style={{ overflowY: isOverflowing ? "scroll" : "auto"   }}>
                {groups.map(group => (
                    <li key={group.id}>
                        <button>+</button>
                        <h1>{group.facult_name}</h1>
                        <h2>{group.course_name} курс</h2>
                        <h3>{group.podgroup_name} группа</h3>
                    </li>
                ))}
            </ul>
        </div>
    )
};
