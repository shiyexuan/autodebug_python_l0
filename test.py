# L0 底线用例：函数实现错误

from sort import bubble_sort, insertion_sort

nums1 = [5, 3, 8, 2, 1]

sorted1 = bubble_sort(nums1)

assert(sorted1 != None)

print("排序后的数组:", sorted1)