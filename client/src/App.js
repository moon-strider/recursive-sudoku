import React, {useState, useEffect} from "react";
import SudokuBoard from "./components/SudokuBoard";
import SudokuLink from "./components/SudokuLink";
import './styles/App.css';

function App() {

  const [data, setData] = useState([{}])

  useEffect(() => {
    fetch("http://127.0.0.1:5000/getpuzzle").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])

  let buttons = [];
  if (data["board"] != undefined & data["board"] != null) {
    for (const [key, value] of Object.entries(data["board"])) {
      buttons.push(value ? value : "-");
    }
  }

  if (data["board"] != undefined & data["board"] != null) {
    return (
      <div className="App">
        <SudokuBoard buttonsInit={buttons}/>
        <SudokuLink/>
      </div>
    );
  }
}

export default App;