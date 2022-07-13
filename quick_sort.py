def quicksort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot=arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot ]
        return quicksort(less) + [pivot] + quicksort(greater)

# making testcases

def test(mine, expected):
    assert mine == expected, f'mine: {mine} vs expected: {expected}'


x = test(quicksort([10, 5, 3, 2]), [2, 3, 5, 10])
print(x)