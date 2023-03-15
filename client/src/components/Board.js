import { createGlobalStyle } from 'styled-components';
import Draggable from 'react-draggable';

import bbPng from './pieces/bb.png';
import bhPng from './pieces/bh.png';
import bkPng from './pieces/bk.png';
import bpPng from './pieces/bp.png';
import bqPng from './pieces/bq.png';
import brPng from './pieces/br.png';
import wbPng from './pieces/wb.png';
import whPng from './pieces/wh.png';
import wkPng from './pieces/wk.png';
import wpPng from './pieces/wp.png';
import wqPng from './pieces/wq.png';
import wrPng from './pieces/wr.png';

const piece_dictionary = {
    'BB': bbPng,
    'BH': bhPng,
    'BK': bkPng,
    'BP': bpPng,
    'BQ': bqPng,
    'BR': brPng,
    'WB': wbPng,
    'WH': whPng,
    'WK': wkPng,
    'WP': wpPng,
    'WQ': wqPng,
    'WR': wrPng, 
}

const BoardStyle = createGlobalStyle`

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

    .board-container {
        display: grid;
        grid-template-columns: 5vw 5vw 5vw 5vw 5vw 5vw 5vw 5vw ;
    }
`

function Board({ gameState }) {

    const state = {
        activeDrags: 0
    }

    const handleDrag = (e, ui) => {
        console.log('handleDrag')
        const {x, y} = ui.deltaPosition || {};
        ui.position = {
          x: x,
          y: y
        };
        console.log(ui.position)
      };

    const onStart = () => {
      ++state.activeDrags
      console.log('onStart')
    };
    
    const onStop = () => {
      --state.activeDrags;
      console.log('onStop');
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