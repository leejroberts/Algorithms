const expect = require('chai').expect;
const _ = require('lodash');

const selectionSort = require('../sorting/selectionSort').selectionSort;

describe('selectionSort', () => {
  let shuffled = _.shuffle([1, 2, 3, 4, 5]);
  it('should return a sorted array', () => {
    expect(selectionSort(shuffled)).to.deep.equal([1, 2, 3, 4, 5]);
  });
});
