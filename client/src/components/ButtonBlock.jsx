import React from "react";
import SudokuButton from "./SudokuButton";

const ButtonBlock = (props) => {

    return (
        <div className="buttonBlock">
            <div className="blockRow">
                <SudokuButton num={props.buttonsInit[0]}/>
                <SudokuButton num={props.buttonsInit[1]}/>
                <SudokuButton num={props.buttonsInit[2]}/>
            </div>
            <div className="blockRow">
                <SudokuButton num={props.buttonsInit[3]}/>
                <SudokuButton num={props.buttonsInit[4]}/>
                <SudokuButton num={props.buttonsInit[5]}/>
            </div>
            <div className="blockRow">
                <SudokuButton num={props.buttonsInit[6]}/>
                <SudokuButton num={props.buttonsInit[7]}/>
                <SudokuButton num={props.buttonsInit[8]}/>
            </div>
        </div>
    )
}

export default ButtonBlock