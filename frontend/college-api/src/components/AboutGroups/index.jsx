import "./style.css";
import axios from "axios";
import { useEffect, useState } from "react";
import getCookie from './../GetCookie/index';

export const AboutGroups = () => {
    const [btnBgF, setbtnBgF] = useState('focus');
    const [btnBgS, setbtnBgS] = useState('nofocus');
    const accessToken = getCookie("accessToken");
    const headers = {
        'Authorization': `Bearer ${accessToken}`,
        'Content-Type': 'application/json'
    };

    // useEffect(() => {
    //     axios.get("http://127.0.0.1:8000/api/v1/data/get_groups", { headers })
    //         .then((response) => {
    //             console.log(response);
    //             // setName(response.data.first_name);
    //         })
    //         .catch((error) => {
    //             console.log(error);
    //         });
    // })

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
        </div>
    )
};
