
const array_1 = [...Array(11).keys()]; // generates an array values 0..10

const bi_search = (search_array, search_value) => {
  let low = 0;
  let high = search_array.length - 1;
  let middle;
  while (true) {
    middle = Math.ceil((low + high) / 2);
    if ( low > high ) {
      return -1;
    } else if (search_value == search_array[middle]) {
      return middle;
    } else if ( search_value < search_array[middle]) {
      high = middle - 1;
    } else if ( search_value > search_array[middle]) {
      low = middle + 1;
    }
  }
};

console.log(bi_search(array_1, 2));
console.log(bi_search(array_1, 2.5));