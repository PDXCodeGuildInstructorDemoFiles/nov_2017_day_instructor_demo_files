function deepestChild() {
    var current = document.getElementById('grand-node').querySelectorAll('div');
    current = Array.apply(null, current);
    console.log(current);
    var next = [];
    while (current) {
        for (var i = 0; i < current.length; i++) {
            if (current[i]) {
                console.log(current[i].innerText.replace(/ /g,''))
                if (current[i].hasChildNodes()) {
                    var childNds = Array.apply(null, current[i].childNodes);
                    for (var k = 0; k < childNds.length; k++) {
                        next.push(childNds[k])
                    }
                }
                if (current[i].innerText === 'boo!') {
                    return current[i].innerText
                }
            }
        }
        current = next.shift()
        // console.log(next)
    }
}

console.log(deepestChild());