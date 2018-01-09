var namesToAges = {
    'Alyssa': 22,
    'Charley': 25,
    'Dan': 25,
    'Jeff': 20,
    'Kasey': 20,
    'Kim': 20,
    'Morgan': 25,
    'Ryan': 25,
    'Stef': 22
};
var agesToNames = {};

for (i in namesToAges) {
    if (namesToAges[i] in agesToNames) {
        agesToNames[namesToAges[i]].push(i)
    } else {
        agesToNames[namesToAges[i]] = new Array(i)
    }
}

var longest = [];
var most_common_age;

for (j in agesToNames) {
    if (agesToNames[j].length > longest.length) {
        longest = agesToNames[j];
        most_common_age = j
    }
}

console.log(longest);
console.log(most_common_age);