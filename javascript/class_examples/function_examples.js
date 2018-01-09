// // console.log('function_examples.js running');
// // // var two = 2;
// // function add2 (x) {
// //     if (arguments.length < 1) {
// //         throw 'The function add2 takes at least one argument. None given.'
// //     }
// //     for (var i=0; i<arguments.length; i++) {
// //         console.log(arguments[i])
// //     }
// //     var two = 2;
// //     return two + x
// // }
// // // console.log(add2(5, 5, 'the', 55.5, 12));
// //
// //
// // try {
// //     add2()
// // } catch (ex) {
// //     console.log(ex)
// // }
// var strArr = ['10.1', '18a2716348712apple', '2.1', '3', '4', '5'];
// var intArr = [];
// for (var i=0;i<strArr.length -1; i++) {
//     intArr.push(parseFloat(strArr[i]))
//     // console.log(strArr[i] - strArr[i + 1])
// }
// // intArr.sort(function (a, b){
// //     return a - b
// // });
// console.log(intArr);
//
// // var int = '5';
// // console.log(parseInt(int) + 5);
// // console.log(int + 5);
//
// var intArr = ['the', 2, 3, 4, 5];
// var strArr = [];
//
// for (var i = 0; i<intArr.length; i++) {
//     strArr.push(String(intArr[i]))
// }
//
// console.log(strArr);
// console.log(isNaN(strArr[0]));

// console.log(Math.abs(100 - 120));
// var name = 'Chris';
// console.log(name.startsWith('D'));

var obj = {
    apple: 1.99,
    pear: 0.99
};

console.log(obj);
console.dir(obj);