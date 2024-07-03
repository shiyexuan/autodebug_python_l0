# L0 底线用例：函数实现错误

from sort import bubble_sort, insertion_sort

nums1 = [5, 3, 8, 2, 1]
nums2 = [5, 8, 3, 2, 1]
bubble_sort(nums1, dec = True)
insertion_sort(nums2, dec = True)
assert(nums1 == nums2)

print("排序后的数组:", nums1)