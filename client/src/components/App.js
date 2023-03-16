import { useEffect, useState } from 'react';
import Board from './Board';
import { createGlobalStyle } from 'styled-components';

const GlobalStyle = createGlobalStyle`
    :root {
      --black: black;
      --white: #bcbbbf;
      --purple: #270973;
      --dark-grey: #111;
    }

    body {
      background-color: var(--dark-grey);
      color: var(--white);
    }
`

function App() {

  const [gameState, setGameState] = useState({
    pieces: '',
    colors: '',
    whites_turn: true
  })

  useEffect(() => {
    fetch('http://127.0.0.1:5555/moves')
      .then(r => r.json())
      .then(data => {setGameState(data[0])})
  }, []);

  function handleMove(fromIndex, toIndex) {
    console.log(fromIndex, toIndex);
    const configObj = {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json",
      },
      body: JSON.stringify({fromIndex, toIndex,}),
    };
    fetch('http://127.0.0.1:5555/moves', configObj)
      .then()
  };

  return (
    <>
      <GlobalStyle />
      <h1>Chess by Kyle</h1>
      <Board 
        gameState={gameState}
        handleMove={handleMove}
      />
    </>
  );
}

export default App;

