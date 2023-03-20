import { useEffect, useState } from 'react';
import { createGlobalStyle } from 'styled-components';

import Board from './Board.js';
import Moves from './Moves.js';
// import test from './test'

const GlobalStyle = createGlobalStyle`
    :root {
      --black: black;
      --white: #bcbbbf;
      --purple: #270973;
      --dark-grey: #111;
      --light-grey: #383838;
    }

    body {
      background-color: var(--dark-grey);
      color: var(--white);
    }

    .game-container {
      display: inline-block;
      width: 100vw;
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
  const [moveData, setMoveData] = useState([
    {index: 0, values: {toIndex: -1, piece: '', color: '', capture: false, castle: ''}}
  ]);

  useEffect(() => {
    fetch('http://127.0.0.1:5555/moves')
      .then(r => r.json())
      .then(data => {setGameState(data.slice(-1)[0])})
  }, []);

  async function handleMove(fromIndex, toIndex) {
    const configObj = {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
        "Accept": "application/json",
      },
      body: JSON.stringify({fromIndex, toIndex,}),
    };

    const newGameState = await fetch('http://127.0.0.1:5555/moves', configObj)
      .then(r => r.json());
    setGameState(newGameState)

    const validMove = !(gameState.pieces == newGameState.pieces);
    
    if (validMove) setMoveData(moves => {
      const index = moves.slice(-1)[0]['index'] + 1
      const values = {
        toIndex: toIndex, 
        piece: newGameState['pieces'][toIndex],
        color: newGameState['colors'][toIndex],
        capture: gameState['pieces'][toIndex] != 'E'
      };
      return [...moves, {index, values} ]
    }); 

    return validMove
  };

  return (
    <>
      <GlobalStyle />
      <h1>Chess by Kyle</h1>
      <div className='game-container'>
        <Board 
          gameState={gameState}
          handleMove={handleMove}
        />
        <Moves moves={moveData}/>
      </div>
    </>
  );
}

export default App;

