import React from "react";
import ButtonBlock from "./ButtonBlock";

const SudokuBoard = (props) => {

    let blocks = [];
    for (let b = 0; b < 9; b++) {
        blocks.push([]);
        let j_shift = b % 3;
        let i_shift = Math.floor(b / 3)*3;
        for (let i = 0; i < 3; i++) {
            for (let j = 0; j < 3; j++) {
                blocks[b].push(props.buttonsInit[(i_shift+i)*9 + (j_shift*3)+j]);
            }
        }
    }
    console.log(blocks);

    return (
        <div className="sudok-board">
            <div className="row-third">
                <ButtonBlock buttonsInit={blocks[0]}/>
                <ButtonBlock buttonsInit={blocks[1]}/>
                <ButtonBlock buttonsInit={blocks[2]}/>
            </div>
            <div className="row-third">
                <ButtonBlock buttonsInit={blocks[3]}/>
                <ButtonBlock buttonsInit={blocks[4]}/>
                <ButtonBlock buttonsInit={blocks[5]}/>
            </div>
            <div className="row-third">
                <ButtonBlock buttonsInit={blocks[6]}/>
                <ButtonBlock buttonsInit={blocks[7]}/>
                <ButtonBlock buttonsInit={blocks[8]}/>
            </div>
        </div>
    )
}

export default SudokuBoard