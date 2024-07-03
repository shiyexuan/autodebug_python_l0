# L0 底线用例：拼写错误

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arrj[1], arr[j]

nums = [5, 3, 8, 2, 1]
bubble_sort(nums)
print("排序后的数组:", nums)