def binary_search(list, item):
    low = 0;
    high = len(list)-1;
    while low <= high:
        mid = (low+high)//2 
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid-1
        else:
            low = low+1
    return None

print(binary_search([1,3,5,7,9], 5))