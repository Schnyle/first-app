import { useState } from 'react';
import { createGlobalStyle } from 'styled-components';
import Draggable from 'react-draggable';

import piece_dictionary from './PiecePngs';

const BoardStyle = createGlobalStyle`

    .board-container {
        height: 40vw;
        width: 40vw;
        display: grid;
        grid-template-columns: repeat(8, 1fr);
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
    }

    .light-square, .dark-square, .trans-square {
        height: 5vw;
        width: 5vw;
        display: flex;
    }

    .trans-square {
      border: 1px solid black;
      opacity: 0;
      height: 100%;
      width: 100%;
      z-index: 1;
    }

    .light-square {
        background-color: var(--white);
    }

    .dark-square {
        background-color: var(--purple);
    }

    img {
      z-index: 0;
    }

`

const getSquares = (posDiff, square_dim) => {
  const posDiffSign = (posDiff > 0 ? 1 : -1)
  let squares = posDiffSign
  if (Math.abs(posDiff) < square_dim / 2) {
    return 0
  };
  posDiff = posDiff - (posDiffSign * square_dim / 2)
  while(Math.abs(posDiff) > square_dim) {
    squares += (posDiffSign)
    posDiff -= (posDiffSign * square_dim)
  };
  return squares
};

function Board({ gameState, handleMove, validMove }) {

    console.log('Board.js', validMove)

    const square_dim_x = window.innerWidth / 20
    const square_dim_y = square_dim_x + 2 // potential problem later on
    let fromIndex;
    let toIndex;

    const state = {
        activeDrags: 0,
        deltaPosition: {x: 0, y: 0},
    }

    const handleDrag = (e, ui) => {
        const {x, y} = state.deltaPosition;
        state.deltaPosition = {
          x: x + ui.deltaX,
          y: y + ui.deltaY
        };
    };
    const onStart = (e, i) => {
        ++state.activeDrags
        fromIndex = i
    };
    const onStop = (e, dragElement) => {
        --state.activeDrags;
        const xSquares = getSquares(state.deltaPosition.x, square_dim_x);
        const ySquares = getSquares(state.deltaPosition.y, square_dim_y);
        toIndex = fromIndex + (8 * ySquares) + xSquares;

        handleMove(fromIndex, toIndex)
        
        if (!validMove) {
          state.deltaPosition = {x:0, y:0}
        } else {
          state.deltaPosition = {x: 1000, y: 1000}
        };
        console.log('dP', state.deltaPosition)
    };

    const pieces_array = gameState.pieces.split('')
    const colors_array = gameState.colors.split('')

    if (pieces_array.length == 0 || colors_array.length == 0) {
        return <></>
    };

    const boardDivs = [];
    
    let row = 0;
    for (let i = 0; i < 64; i++) {
        // set color
        let shade;
        if ((i % 2 == 0 && row % 2 == 0) || (i % 2 == 1 && row % 2 == 1)) {
            shade = 'light'
        } else shade = 'dark';

        // set piece
        let piecePng;
        if (colors_array[i] == 'E') {
            piecePng = ''
        } else {
            const color = colors_array[i];
            const piece = pieces_array[i];
            piecePng = piece_dictionary[`${color}${piece}`]
        };

        const square_id = `square${i}`;
        boardDivs.push(
          <div 
            className={`${shade}-square`} 
            key={i}
          >
            <Draggable 
              onDrag={handleDrag}
              onStart={(e) => onStart(e, i)}
              onStop={onStop}
              bounds='.board-container'
              position={{x: state.deltaPosition.x, y: state.deltaPosition.y}}
            >
              <img draggable='false' src={piecePng} />
            </Draggable>
            <div 
              id={square_id} 
              className='trans-square' 
            ></div>
          </div>
        )
        
        if ((i + 1) % 8 == 0) {
            row += 1
        };

    }

    return (
        <>
          <BoardStyle />
          <div className='board-container'>
            {boardDivs}
          </div>
        </>
    );
}

export default Board;