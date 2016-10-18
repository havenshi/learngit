import bisect
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        for i in range(len(nums2)):
            bisect.insort(nums1, nums2[i])

        if len(nums1)%2==0:
            return float((nums1[(len(nums1))/2-1]+nums1[(len(nums1))/2])/2.0)
        else:
            return nums1[(len(nums1)-1)/2]/1.0


if __name__=="__main__":
    answer=Solution()
    nums1=[1,3]
    nums2=[2]
    print answer.findMedianSortedArrays(nums1,nums2)