
# time complexity O(n^2)
#space complexity O(n)


def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr):
    newArr = []
    for _ in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr


def test(mine,expected):
    return "passed" if mine == expected else f'mine: {mine} vs expected: {expected}'

if __name__ == "__main__":
    print(test([2, 3, 5, 6, 9], selectionSort([6, 9, 2, 3, 5])))