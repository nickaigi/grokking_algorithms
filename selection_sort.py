def selection_sort(arr: list) -> None:
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


if __name__ == '__main__':
    arr: list = [5, 3, 6, 2, 10]
    selection_sort(arr=arr)

    assert arr == [2, 3, 5, 6, 10]
