# GOIT-ALGO2-HW-01

## Project Description

This repository contains two implemented functions that use the "divide and conquer" method to perform search tasks in an array:

1. **find_min_max** – A function that finds the minimum and maximum elements in an array.
2. **quick_select** – A function that finds the k-th smallest element in an array using the Quick Select method.

## Implementation Details

### part_1: find_min_max

The `find_min_max` function splits the array into two parts, recursively finds the minimum and maximum in each half, and then merges the results.

- Uses a recursive approach.
- Time complexity: **O(n)**.

### part_2: quick_select

The `quick_select` function finds the k-th smallest element in an array using the Quick Select principle.

- The method is based on selecting a pivot element and partial sorting.
- Does not require full sorting of the array.
- Average time complexity: **O(n)**.

## Usage

```python
arr = [3, 1, 7, 9, 2, 8, 5, 6]
k = 3
print(find_min_max(arr))
print(quick_select(arr, k))
```

## Requirements

- Python 3.x

## Author

- Eduard Schumacher
