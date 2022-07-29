import React, {useState, useEffect} from "react";
import Button from "./components/Button";
import SudokuBoard from "./components/SudokuBoard";
import SudokuLink from "./components/SudokuLink";
import './styles/App.css';

function App() {

  const [data, setData] = useState([{}]);
  const [buttons, setButtons] = useState([]);
  const [loading, setLoading] = useState(false);
  const [solving, setSolving] = useState(false);

  useEffect(() => {
    getpuzzle()
  }, [])

  async function getpuzzle() {
    setLoading(true);
    await fetch("/getpuzzle")
    .then( res => res.json() )
    .then( data => { setData(data) } )
    setLoading(false);
  }

  async function solvepuzzle() {
    setSolving(true);
    const fetchOptions = {
      method: 'POST',
      headers: {'content-type': 'application/json',},
      body: JSON.stringify(data)
    }
    await fetch("/solvepuzzle", fetchOptions,)
    .then( res => res.json() )
    .then( data => { setData(data) } )
    setSolving(false);
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
        <div class="button-row">
          <Button loading={solving} onClick={solvepuzzle} text={"Solve"}/>
          <Button loading={loading} onClick={getpuzzle} text={"Refresh"}/>
        </div>
        <SudokuLink/>
      </div>
    );
  }
}

export default App;