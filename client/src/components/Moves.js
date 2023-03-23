import { createGlobalStyle } from "styled-components";

// ♟ black pawn
// ♙ white pawn

const piece_dictionary_text = {
    'BB': '♗',
    'BH': '♘',
    'BK': '♔',
    'BP': '',
    'BQ': '♕',
    'BR': '♖',
    'WB': '♝',
    'WH': '♞',
    'WK': '♚',
    'WP': '',
    'WQ': '♛',
    'WR': '♜', 
}

const MovesStyle = createGlobalStyle`
    .moves-container {
        height: 40vw;
        width: 20vw;
        background-color: var(--light-grey);
        margin-left: 5vw;
        border-radius: 5%;
    }


    h2 {
        text-align: center;
    }
`

const posToCoord = (position) => {
    const row_index = (position % 8);
    const row = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'][row_index]
    const col = 8 - Math.floor(position / 8);
    return `${row}${col}`
};

const reshape = (array) => {
    const result = [];
    let tempArray = [];
    let i = 0;
    for (const element of array) {
        tempArray.push(element);
        if (tempArray.length == 2) {
            result.push([i, ...tempArray]);
            tempArray = [];
        };
        i++;
    };

    if (tempArray.length == 1) result.push([i, ...tempArray]);
    
    return result
};

function Moves({ moves }) {

    const moveStrings = moves.slice(1).map(move => {
        if (move['values']['castle'] == 'short') return 'O-O';
        if (move['values']['castle'] == 'long') return 'O-O-O';
        
        const color = move['values']['color'];
        const piece = move['values']['piece'];
        const capture = move['values']['capture'];
        const fromCoord = posToCoord(move['values']['fromIndex']);
        const toCoord = posToCoord(move['values']['toIndex']);
        
        let pieceText;
        pieceText = piece_dictionary_text[`${color}${piece}`];
        
        if (piece == 'P' && capture) pieceText = fromCoord[0];

        return `${pieceText}${capture ? 'x' : ''}${toCoord}`
    });

    const moveStringsByTwo = reshape(moveStrings);

    const moveList = moveStringsByTwo.map(moveTriple => {
        return (
            <li key={moveTriple[0]}>
                {moveTriple[1]} {moveTriple[2]}
            </li>
        );
    });

    return (
        <>
            <MovesStyle />
            <div className='moves-container'>
                <h2>Moves</h2>
                <ol>{moveList}</ol>
            </div>
        </>
    );
}

export default Moves;