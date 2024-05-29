import { useState, useEffect } from "react";
import { Checkbox, Divider } from "antd";

const CheckboxGroup = Checkbox.Group;
const plainOptions = ["Факультет", "Курс", "Подгруппа"];
const defaultCheckedList = [];

export const ChooseSortGroups = ({ getSortInfo }) => {
    const [checkedList, setCheckedList] = useState(defaultCheckedList);

    useEffect(() => {
        getSortInfo(checkedList);
    }, [checkedList, getSortInfo]);

    const checkAll = plainOptions.length === checkedList.length;
    const indeterminate = checkedList.length > 0 && checkedList.length < plainOptions.length;

    const onChange = (list) => {
        setCheckedList(list);
    };

    const onCheckAllChange = (e) => {
        setCheckedList(e.target.checked ? plainOptions : []);
    };

    return (
        <>
            <Checkbox
                indeterminate={indeterminate}
                onChange={onCheckAllChange}
                checked={checkAll}
            >
                Выбрать все
            </Checkbox>
            <Divider />
            <CheckboxGroup
                options={plainOptions}
                value={checkedList}
                onChange={onChange}
            />
        </>
    );
};
