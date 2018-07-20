/* how selection sort works

starting at the zero index, find the lowest value in the array
move the first value to the lowest value, and the lowest value to the first value

starting at the next index, repeat above procedure

continue until outer loop reaches the end of the array

*/

module.exports.selectionSort = arr => {
  for (let startingI = 0; startingI < arr.length; startingI++) {
    let lowestI = startingI; // the index with the lowest value defaults to the first index

    // find the index of the lowest value
    for (let compareI = startingI + 1; compareI < arr.length; compareI++) {
      if (arr[lowestI] >= arr[compareI]) {
        lowestI = compareI;
      }
    }

    // switch the values of the lowest index and the starting index, if they are not the same
    if (lowestI !== startingI) {
      let tempVal = arr[startingI];
      arr[startingI] = arr[lowestI];
      arr[lowestI] = tempVal;
    }
  }
  return arr;
};
