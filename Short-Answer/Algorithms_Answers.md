#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) I first thought this to be a polynomial time complexity, but I believe it is linear; O(n). This is because the while loop utilizes (a < n^3), but inside the loop a increases by (a + n^2).


b) This code snippet is a linearithmic, O(n log n), time complexity. This is because we have a loop that iterates `n` times, with a nested loop that has an logarithmic O(log n) time complexity.


c) `bunnyEars` has a linear O(n) time complexity since it will recursivley call itself `n` times.

## Exercise II

- For this problem I want to find `f` which is the floor that eggs begin to break on.
- I could implement a recursive solution that starts by checking the middle floor of the building.
- If the egg breaks then I can call the function on the lower half of the building and so forth.
- If the egg does not break then I will call on the upper half of the building.
- I will need to store both the `lowest_floor` that the egg breaks, and the `highest_floor` at which it does not.
  - once I have these I will iterate from lowest to highest until I find the first floor, `f`, that the egg begins to break and return it.

This solution would have a worst case time complexity of O(n) since I divide the number of floors, O(log n), then iterate over a portion of them, O(n).
