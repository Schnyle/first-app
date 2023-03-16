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

    .light-square {
        height: 5vw;
        background-color: var(--white);
        display: flex;
    }

    .dark-square {
        height: 5vw;
        background-color: var(--purple);
        display: flex;
    }

    .img {
        height: 5vw;
        width: 5vw;
        margin: 0;
    }

`

function Board({ gameState }) {
    const state = {
        activeDrags: 0
    }

    const handleDrag = (e, ui) => {
        const {x, y} = ui.deltaPosition || {};
        ui.position = {
            x: x,
            y: y
        };
    };
    const onStart = () => {
        ++state.activeDrags
    };
    const onStop = () => {
        --state.activeDrags;
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

        boardDivs.push(
          <div className={`${shade}-square`} key={i}>
            <Draggable 
              onDrag={handleDrag}
              onStart={onStart}
              onStop={onStop}
              bounds='.board-container'
              // offsetParent={document.querySelector('.board-container')}
            >
              <img draggable='false' src={piecePng}/>
            </Draggable>
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