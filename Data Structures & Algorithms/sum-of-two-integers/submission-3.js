class Solution {
  /**
   * @param {number} a
   * @param {number} b
   * @return {number}
   */
  getSum (a, b) {
    while (b !== 0) {
      let carry = (b & a) << 1
      a ^= b
      b = carry
    }
    return a
  }
}
