import { useEffect, useState } from 'react';

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

  return (
    <h1>{gameState.pieces}</h1>
  );
}

export default App;
