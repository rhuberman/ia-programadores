
/**
 * Sorts an array using the Bubble Sort algorithm.
 * 
 * @param {Array} arr - The input array to be sorted.
 * @returns {Array} A new sorted array in ascending order.
 * 
 * @example
 * const unsorted = [64, 34, 25, 12, 22, 11, 90];
 * const sorted = bubbleSort(unsorted);
 * // sorted is now [11, 12, 22, 25, 34, 64, 90]
 */
function bubbleSort(arr) {
    // Make a copy of the array to avoid modifying the original
    const array = [...arr];
    const n = array.length;
    
    // Outer loop to control the number of passes
    for (let i = 0; i < n - 1; i++) {
      // Inner loop to perform comparisons and swaps
      for (let j = 0; j < n - i - 1; j++) {
        // Compare adjacent elements
        if (array[j] > array[j + 1]) {
          // Swap elements if they are in wrong order
          [array[j], array[j + 1]] = [array[j + 1], array[j]];
        }
      }
    }
    
    // Return the sorted array
    return array;
  }
  
  // Example usage
  const unsortedArray = [64, 34, 25, 12, 22, 11, 90];
  const sortedArray = bubbleSort(unsortedArray);
  console.log("Original array:", unsortedArray);
  console.log("Sorted array:", sortedArray);