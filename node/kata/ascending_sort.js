"use strict";

// system of sorting
//     find max in array
//     add it to new sorted_array, remove it from array
//     repeat until array is empty
//     (I avoided using methods with less full support, likely this can be done quicker)

var array = [ 55, 23, 26, 2, 25 ];

function findMin(arr) {
    var min = arr[0];
    var a = arr.length;
    for ( var counter = 0 ;counter < a; counter++ ) {
        if ( array[counter] < min ) {
            min = array[counter];
        }
    }
    return min;
}

function sortMin(arr) {
    var sorted_array = [];
    while( arr.length > 0) {
        var min = findMin(arr);
        sorted_array.push(min);
        arr.splice(arr.indexOf(min), 1);
    }
    return sorted_array;
}


console.log( sortMin(array) );