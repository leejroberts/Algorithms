const expect = require('chai').expect;
const _ = require('lodash');
const insertionSort = require('../sorting/insertionSort').insertionSort;

describe('insertionSort', () => {
  it('should return a sorted array', () => {
    let shuffledArr = _.shuffle([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
    let sortedArr = insertionSort(shuffledArr);
    expect(sortedArr).to.eql([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
  });
});
