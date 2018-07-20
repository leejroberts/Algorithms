var array_1 = [ [1,5], [2, 10], [22, 45], [2, 5], [64, 66], [2, 8], [19, 23], [78, 79], [22, 22], [12, 14], [ 35, 58 ], [0,1], [1000, 1001] ];

for( var index = 0; index < array_1.length; index++){
    var current_array = array_1.splice(index, 1);
    console.log(current_array);
    console.log(array_1);

    current_array = [].concat.apply([], current_array);
    
    for (var i = 0; i < array_1.length ; i++ ){
        if ( current_array[0] <= array_1[i][0] && current_array[1] >= array_1[i][0] && current_array[0] <= array_1[i][1] && current_array[1] >= array_1[i][1] ){
            array_1.splice(i, 1); 
            
        } else if ( current_array[0] <= array_1[i][0] && current_array[1] >= array_1[i][0] ){
            current_array.splice(1, 1, array_1[i][1]);
            array_1.splice(i, 1); 
            
        } else if ( current_array[0] <= array_1[i][1] && current_array[1] >= array_1[i][1] ){
            current_array.splice( 0, 1, array_1[i][0]);
            array_1.splice(i, 1);
        }
    }
    array_1.splice(index, 0, current_array);
    console.log(current_array);
    console.log(array_1);
}

