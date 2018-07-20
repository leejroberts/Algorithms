var array_1 = [ [1,5], [2, 10], [22, 45], [2, 5], [64, 66], [45, 77], [6,7], [22, 23], [33, 45], [66,67], [18, 22], [19, 22] ];

var merger = function(array_1, index){
    if ( array_1.length - 1 == index){
        return array_1;
    }
    
    var current_array = array_1.splice(index, 1);
    current_array = [].concat.apply([], current_array); //flattens the array
    
    console.log(current_array);
    console.log(array_1);
    for (var i = 0; i < array_1.length ; i++ ){
        if ( current_array[0] < array_1[i][0] && current_array[1] > array_1[i][0] && current_array[0] < array_1[i][1] && current_array[1] > array_1[i][1] ){
            array_1.splice(i, 1); 
            
        } else if ( current_array[0] < array_1[i][0] && current_array[1] > array_1[i][0] ){
            current_array.splice(1, 1, array_1[i][1]);
            array_1.splice(i, 1); 
            
        } else if ( current_array[0] < array_1[i][1] && current_array[1] > array_1[i][1] ){
            current_array.splice( 0, 1, array_1[i][0]);
            array_1.splice(i, 1);
        }
    }
    
    array_1.splice(index, 0, current_array);
    index++;
    merger(array_1, index);
};


console.log( merger(array_1, 0) );
