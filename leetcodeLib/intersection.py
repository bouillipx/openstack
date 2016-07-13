__author__ = 'bouilli'
def intersection1(nums1, nums2):
    return list(set(nums1)&set(nums2))

def intersection2(nums1, nums2):
    result = []
    for num in nums1:
        if num in nums2:
            nums1.remove(num)
            result.append(num)
    return result