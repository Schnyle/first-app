const one = [
    "e4",
    "e5",
    "♘f3"
]

const two = [
    "e4",
    "e5",
    "♘f3",
    "♝b4"
]

function reshape(array) {
    const result = [];
    let tempArray = [];
    for (const element of array) {
        tempArray.push(element);
        if (tempArray.length == 2) {
            result.push(tempArray);
            tempArray = [];
        };
    };

    if (tempArray.length == 1) result.push(tempArray);
    
    return result
};

console.log('one', reshape(one))
console.log('two', reshape(two))