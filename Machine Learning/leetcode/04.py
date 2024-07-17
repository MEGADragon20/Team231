def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
    for i in nums1:
        nums2.append(i)
    nums2.sort()
    a = len(nums2)
    if a%2 == 1:
        return nums2[int(a+1/2)-1]
    else:
        return (nums2[int(a/2)-1] + nums2[int(a/2)]) / 2

        