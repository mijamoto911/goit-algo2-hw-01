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


def quick_select(arr, k):
    def partition(left, right):
        pivot = arr[right]
        i = left
        for j in range(left, right):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1
        arr[i], arr[right] = arr[right], arr[i]
        return i

    def select(left, right, k):
        if left == right:
            return arr[left]
        pivot_index = partition(left, right)
        if k == pivot_index:
            return arr[k]
        elif k < pivot_index:
            return select(left, pivot_index - 1, k)
        else:
            return select(pivot_index + 1, right, k)

    if k < 1 or k > len(arr):
        raise ValueError("k must be within the length of the array")

    return select(0, len(arr) - 1, k - 1)


arr = [3, 1, 7, 9, 2, 8, 5, 6, 0, 4, 8]
k = 3
print(find_min_max(arr))
print(quick_select(arr, k))
