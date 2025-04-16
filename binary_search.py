from typing import List, Optional


def binary_search(arr: List[int], item: int) -> Optional[int]:
    low: int = 0
    high: int = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == '__main__':
    arr: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    item = 8

    assert binary_search(arr=arr, item=8) == 7
    assert binary_search(arr=arr, item=11) is None
