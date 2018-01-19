const outerFunc = (function () {
    let accum = 0;
    const innerFuncExp = function () {
        return accum += 1
    };
    return innerFuncExp
})();


console.dir(outerFunc);
console.log(outerFunc());

console.dir(outerFunc);
console.log(outerFunc());

console.dir(outerFunc);
console.log(outerFunc());