from itertools import combinations as C


def reunion(even, odd):
    # generate first "odd" odd numbers [1,3,5]
    oddN = [i for i in range(1, (odd * 2) + 1) if i % 2 != 0]
    # generate first "even" even numbers [2,4]
    evenN = [i for i in range(1, (even * 2) + 1) if i % 2 == 0]
    odds = [list(C(oddN, i)) for i in range(1, len(oddN) + 1)]
    odds = [j for i in odds for j in i]
    oddpics = [(s,) + i for i in odds for s in evenN if all([s > v for v in i])]
    print(f"Odd number pictures: {oddpics}")
    evens = [list(C(evenN, i)) for i in range(1, len(evenN) + 1)]
    evens = [j for i in evens for j in i]
    evenpics = [
        (s,) + i for i in evens for s in oddN if all([s > v for v in i])]
    print(f"Even number pictures: {evenpics}")
    return len(oddpics + evenpics)


# v = reunion(2, 2)
# print(v)

def quickSort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        low = [i for i in arr[1:] if i <= pivot]
        high = [i for i in arr[1:] if i > pivot]
        return quickSort(low) + [pivot] + quickSort(high)


def findSmallest(arr):
    sm = arr[0]
    ind = 0
    for i in range(len(arr)):
        if a[i] < sm:
            sm = a[i]
            ind = i
    return ind


def selectionSort(arr):
    new_arr = []
    for i in range(len(arr)):
        new_arr.append(arr.pop(findSmallest(arr)))
    return new_arr


def binarySearch(arr, n):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == n:
            return mid
        if guess > n:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def rBinarySearch(arr, n, low=0, high=len(arr)):
    print(low)
    if low > high:
        return -1
    else:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == n:
            return mid
        if guess > n:
            return rBinarySearch(arr, n, low, mid - 1)
        else:
            return rBinarySearch(arr, n, mid + 1, high)


a = [1, 2, 0, 3, 5, 1, 3, 6, 7, 8]
p = selectionSort(a)
print(p)
print(rBinarySearch(p, 3))
