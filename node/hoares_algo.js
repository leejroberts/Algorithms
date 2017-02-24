'use strict';

let partition = function(arr, low, high) {
  let pivot_value = arr[low];
  let i = low;
  let j = high;

  while (i < j) {
    while (arr[i] <= pivot_value && i <= high) {
      i++;
    }

    while (arr[j] > pivot_value) {
      j--;
    }

    if (i < j) {
      // swap arr[i], arr[j]
      let temp = arr[i];
      arr[i] = arr[j];
      arr[j] = temp;
    } else {
      break;
    }

  }

  arr[low] = arr[j];
  arr[j] = pivot_value;

  // return the pivot index
  return j;
};

let quick_sort_rec = function(a, l, h) {
  if (h > l) {
    let pivot_index = partition(a, l, h);
    quick_sort_rec(a, l, pivot_index - 1);
    quick_sort_rec(a, pivot_index + 1, h);
  }
};

let quick_sort = function(a) {
  quick_sort_rec(a, 0, a.length - 1);
};

var array = [10, 7, 15, 4, 1 ,2 ,3 ,5, 1000, 0, 79, 5];

var array = quick_sort(array);

console.log(array);