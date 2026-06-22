class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)+len(nums2)
        nums = []
        count_1 = 0
        count_2 = 0
        res = 0

        for i in range(n):
            if count_1 == len(nums1):
                nums.append(nums2[count_2])
                count_2 += 1

            elif count_2 == len(nums2):
                nums.append(nums1[count_1])
                count_1 += 1
                

            elif nums1[count_1] <= nums2[count_2]:
                nums.append(nums1[count_1])
                count_1 += 1
            else:
                nums.append(nums2[count_2])
                count_2 += 1

        if n%2:
            m = n//2
            res = nums[m]
        else:
            m1 = n//2
            m2 = m1 - 1
            res = (nums[m1] + nums[m2])/2

        return res



            