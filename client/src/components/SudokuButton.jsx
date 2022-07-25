import React from "react";
import { useState } from "react";

const SudokuButton = (props) => {
    const [num, setNum] = useState(props.num);

    return (
        <button className="btn">
            {num}
        </button>
    )
}

export default SudokuButton