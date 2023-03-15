import { createGlobalStyle } from 'styled-components';
import bbPng from './pieces/bb.png';

const BoardStyle = createGlobalStyle`
    .row-container {
        display: flex;
    }

    .light-square {
        height: 100px;
        width: 100px;
        background-color: var(--white);
    }

    .dark-square {
        height: 100px;
        width: 100px;
        background-color: var(--purple);
    }

    .img {
        height: 200px;
        width: 200px;
    }
`

function Board() {
    
    const rowA = (
        <div className='row-container'>
          <div className="light-square">
            <img src={bbPng}/>
          </div>
          <div className="dark-square"></div>
          <div className="light-square"></div>
          <div className="dark-square"></div>
          <div className="light-square"></div>
          <div className="dark-square"></div>
          <div className="light-square"></div>
          <div className="dark-square"></div>
        </div>
    );

    const rowB = (
        <div className='row-container'>
          <div className="dark-square"></div>
          <div className="light-square"></div>
          <div className="dark-square"></div>
          <div className="light-square"></div>
          <div className="dark-square"></div>
          <div className="light-square"></div>
          <div className="dark-square"></div>
          <div className="light-square"></div>
        </div>
    );
    
    return (
        <>
          <BoardStyle />
          <div className="board-container">
            {rowA}
            {rowB}
            {rowA}
            {rowB}
            {rowA}
            {rowB}
            {rowA}
            {rowB}
          </div>
        </>
    );
}

export default Board;