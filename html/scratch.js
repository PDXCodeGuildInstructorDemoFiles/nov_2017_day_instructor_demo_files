function almostIncreasingSequence(sequence) {
    emptyArray = [];
    duplicateCheckArray = [];
    sequence.map(Number);
    let counter = 0;
    for (let i = 0; i < sequence.length; i++) {
        if (sequence[i] >= sequence[i + 1]) {
            counter += 1;
            for (x = i + 1; x < sequence.length; x++) {
                if (sequence[x] >= sequence[i]) {
                    console.log(sequence[x]);
                    console.log(sequence[i]);
                    return false
                }
            }
        }
        else if (counter > 1) {
            return false
        }
    }
    return true
}


console.log(almostIncreasingSequence([0, -2, 5, 6]));

// console.log(almostIncreasingSequence([123, -17, -5, 1, 2, 3, 12, 43, 45]))

// console.log(almostIncreasingSequence([3, 5, 67, 98, 3]))