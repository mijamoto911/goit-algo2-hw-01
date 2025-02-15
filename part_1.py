def find_min_max(arr):
    def divide_and_conquer(arr, left, right):
        if left == right:
            return arr[left], arr[left]

        if right - left == 1:
            if arr[left] < arr[right]:
                return arr[left], arr[right]

        mid = (left + right) // 2
        left_min, left_max = divide_and_conquer(arr, left, mid)
        right_min, right_max = divide_and_conquer(arr, mid + 1, right)

        return min(left_min, right_min), max(left_max, right_max)

    if not arr:
        raise ValueError("Array have't to be empty")

    return divide_and_conquer(arr, 0, len(arr) - 1)


arr = [3, 1, 7, 9, 2, 8, 5, 6, 0, 4, 8]
print(find_min_max(arr))
