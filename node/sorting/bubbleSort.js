// creates an ascending sort via bubble sort
// big O notation for time complexity is O(N^2) or quadratic

function bubbleSort(arr) {
  let stepCount = 0;
  let lastIndexToCheck = arr.length - 2;

  while (true) {
    let switchCount = 0;
    for (let i = 0; i <= lastIndexToCheck; i++) {
      stepCount++;
      let nextIndex = i + 1;
      if (arr[i] > arr[nextIndex]) {
        // reverse the values of the two indices
        let tempVal = arr[i];
        arr[i] = arr[nextIndex];
        arr[nextIndex] = tempVal;
        switchCount++;
      }
    }
    lastIndexToCheck--;
    if (switchCount === 0 || lastIndexToCheck < 0) {
      break;
    }
  }
  console.log('sorted array:', arr);
  console.log('number of steps:', stepCount);
}

let arrie1 = [5, 4, 3, 2, 1];
bubbleSort(arrie1);

let arrie2 = [1, 2, 3, 4, 5];
bubbleSort(arrie2);
