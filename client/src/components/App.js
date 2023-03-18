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
    whites_turn: true,
    toIndex: null,
    fromIndex: null
  })

  useEffect(() => {
    fetch('http://127.0.0.1:5555/moves')
      .then(r => r.json())
      .then(data => {setGameState(data.slice(-1)[0])})
  }, []);

  const [validMove, setValidMove] = useState(false);

  async function handleMove(fromIndex, toIndex) {
    const configObj = {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json",
      },
      body: JSON.stringify({fromIndex, toIndex,}),
    };
    await fetch('http://127.0.0.1:5555/moves', configObj)
      .then(r => r.json())
      .then(newGameState => {
        // do this better jeez
        const gameStateNoId = {...gameState}
        delete gameStateNoId.id
        delete gameStateNoId.fromIndex
        delete gameStateNoId.toIndex
        const newGameStateNoId = {...newGameState}
        delete newGameStateNoId.id
        delete newGameStateNoId.fromIndex
        delete newGameStateNoId.toIndex
        setGameState(newGameState)
        setValidMove(!(JSON.stringify(gameStateNoId) == JSON.stringify(newGameStateNoId)));
      })
      .then(() => {return validMove})
      // console.log('App.js', validMove)
  };

  return (
    <>
      <GlobalStyle />
      <h1>Chess by Kyle</h1>
      <Board 
        gameState={gameState}
        handleMove={handleMove}
        validMove={validMove}
      />
    </>
  );
}

export default App;

