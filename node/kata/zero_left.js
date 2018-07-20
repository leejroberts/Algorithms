var array = [1, 10, 20, 0, 59, 62, 0, 88, 0];


for(var counter = 0; counter < array.length; counter++) {
    if (array[counter] == 0) {
        array.splice(counter, 1);
        array.unshift(0);
    }
}

console.log(array);



