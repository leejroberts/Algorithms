// the first array of non negative integers. The second array is the first array shuffled
// with one integer removed.
// find the missing integer.


function findMissing(arr_1, arr_2) {
  arr_1 = arr_1.sort((a,b)=>a - b);
  arr_2 = arr_2.sort((a,b)=>a - b);
  for (let i = 0; i < arr_2.length; i++) {
    // loops through all the indices of array_2 looking for a mismatch.
    if (arr_1[i] !== arr_2[i] ) {
      return arr_1[i];
    }
  }
  return arr_1[arr_1.length -1];
  // if no mismatches are found, the missing item is the last integer.
}

let test_arr_1 = [2,4,3,1,5,10];
let test_arr_2 = [4,3,1,2,10];

console.log(findMissing(test_arr_1, test_arr_2));
// missing is 5.

let test_2_arr_2 = [1,5,3,2,4];

console.log(findMissing(test_arr_1, test_2_arr_2));
// missing is 10, the last int.
