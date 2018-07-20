

let array_1 = [...Array(11).keys()];


const binary_search = (search_array, search_value, low=0, high=null) => {
  high = high || search_array.length - 1;
  let middle = Math.ceil((low + high) / 2);
  if (low > high) {
    return -1;
  } else if (search_value == search_array[middle]) {
    return middle;
  } else if (search_value < search_array[middle]) {
    high = middle - 1;
  } else if (search_value > search_array[middle]) {
    low = middle + 1;
  }
  return binary_search(search_array, search_value, low, high);
  // return statement needed to get the result to "trickle down"
};

console.log(binary_search(array_1, 2));
console.log(binary_search(array_1, 2.5));