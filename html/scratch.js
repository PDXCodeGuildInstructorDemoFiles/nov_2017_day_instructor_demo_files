let test = [1, 2, 3, 4, 99, 5, 6];
let tempArr = [];

for (let i = 0; i < test.length; i++) {
    if (test[i] < test[i + 1]) {
        tempArr = test.slice();
        tempArr.splice(i, 1)
    }
}

console.log(tempArr);