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
            a=(nums1[(len(nums1))/2-1]+nums1[(len(nums1))/2])/2.00
            return '%.5f'% a
        else:
            a=nums1[(len(nums1)-1)/2]
            return '%.1f' % a


if __name__=="__main__":
    answer=Solution()
    nums1=[1,2]
    nums2=[3,4]
    print answer.findMedianSortedArrays(nums1,nums2)