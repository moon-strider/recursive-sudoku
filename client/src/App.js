import React, {useState, useEffect} from "react";
import SolveButton from "./components/SolveButton";
import SudokuBoard from "./components/SudokuBoard";
import SudokuLink from "./components/SudokuLink";
import './styles/App.css';

function App() {

  const [data, setData] = useState([{}]);
  const [buttons, setButtons] = useState([]);

  useEffect(() => {
    fetch("/getpuzzle")
    .then( res => res.json() )
    .then( data => { setData(data) } )
  }, [])

  function solvepuzzle() {
    const fetchOptions = {
      method: 'POST',
      headers: {'content-type': 'application/json',},
      body: JSON.stringify(data)
    }
    fetch("/solvepuzzle", fetchOptions,)
    .then( res => res.json() )
    .then( data => { setData(data) } )
  }
  
  useEffect(
    () => {
      let tmp_buttons = []
      if (data["board"] != undefined) {
        for (const [key, value] of Object.entries(data["board"])) {
          tmp_buttons.push(value != "0" ? value : "");
        }
      console.log(tmp_buttons)
      setButtons(tmp_buttons);
      }
    }
  , [data]);

  if (buttons[0] != undefined) {
    return (
      <div className="App">
        <SudokuBoard buttonsInit={buttons}/>
        <SolveButton onClick={solvepuzzle}/>
        <SudokuLink/>
      </div>
    );
  }
}

export default App;