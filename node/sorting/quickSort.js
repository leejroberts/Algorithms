function partition(arr, low_i = 0, high_i = arr.length - 1) {
  let pivot_i = high_i;
  let pivot_value = arr[pivot_i];
  high_i--;
  while (true) {
    while (arr[low_i] < pivot_value) {
      low_i++;
    }
    while (arr[high_i] > pivot_value) {
      high_i--;
    }
    if (low_i > high_i) {
      break;
    } else {
      let temp_value = arr[low_i];
      arr[low_i] = arr[high_i];
      arr[high_i] = temp_value;
    }
    let temp_value = arr[low_i];
    arr[low_i] = arr[pivot_i];
    arr[pivot_i] = arr[low_i];
  }
  return low_i;
}

function quickSort(arr, low_i = 0, high_i = arr.length - 1) {
  if (low_i - high_i <= 0) {
    // segment contains 1 or fewer indices to check
    return; // there is nothing to return, this exits the function
  }
  let pivot_i = partition(arr, low_i, high_i);
  quickSort(arr, low_i, pivot_i - 1);
  quickSort(arr, pivot_i + 1, high_i);
}
