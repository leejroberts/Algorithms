"use strict";

var string1 = 'Here is a string!';

var reverse_string = function(str) {
    return str.split(' ').reverse().join(' ');
};

console.log(reverse_string(string1));

// challenge_2 without reverse

var reverse_string2 = function(str){
    var string_array = str.split(' ');
    var reverse_array = [];
    for( var i = 0; i < string_array.length; i++ ){
        reverse_array.unshift( string_array[i] );
    }
    return reverse_array.join(' ');
};

console.log(reverse_string2(string1));


