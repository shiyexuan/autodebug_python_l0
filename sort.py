def insertion_sort(arr, dec = False):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and (arr[j] < key if dec else arr[j] > key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def bubble_sort(arr, dec = False):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if (arr[j] < arr[j + 1] if dec else arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]