import React from "react";

const SudokuButton = (props) => {
    return (
        <button className="btn">
            {props.num}
        </button>
    )
}

export default SudokuButton