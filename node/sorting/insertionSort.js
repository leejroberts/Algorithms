/*

insertion sort:

basic idea: it pops out the values (moving left to right)
  if the previous values are greater, it moves them over over 1 spot,
  if not, it re-inserts the value at it's original position

*/

module.exports.insertionSort = arr => {
  // loop over each index
  for (let index = 1; index < arr.length; index++) {
    let position = index; // allows moving backwards through array without disturbing index
    let compare_value = arr[index]; // value for the index at the start of comparison

    // while the position is not the first in the array (0),
    // and if the value from 1 ahead of the position is larger than the value at the postition (thus out of order)
    while (position > 0 && compare_value < arr[position - 1]) {
      // move the value from one ahead of the position into the position (move it up one index)
      arr[position] = arr[position - 1];
      // decrement position and repeat
      position--;
    }
    // once the values ahead of the compare value are shifted as necessary,
    // put the compare_value into the "empty" slot (it might not move at all)
    arr[position] = compare_value;
  }
  // once all indicies are checked and in order, return the mutated array
  // note that return is not needed, as the original array has been mutated
  return arr;
};
