function findMissing(arr_1, arr_2) {
  return  (arr_1.reduce((sum, item)=>sum + item) - 
           arr_2.reduce((sum, item)=>sum + item))
}

let test_arr_1 = [2,4,3,1,5,10];
let test_arr_2 = [4,3,1,2,10];

console.log(findMissing(test_arr_1, test_arr_2));
// missing is 5.

let test_2_arr_2 = [1,5,3,2,4];

console.log(findMissing(test_arr_1, test_2_arr_2));
// missing is 10, the last int.
 
