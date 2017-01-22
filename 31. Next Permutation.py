# -*- coding: utf-8 -*-
# 1. From right to left, find the first digit (PartitionNumber) which violate the increase trend.
# 2. From right to left, find the first digit which larger than PartitionNumber, call it ChangeNumber.
# 3. Swap the PartitionNumber and ChangeNumber.
# 4. Reverse all the digit on the right of partition index.
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] < nums[i + 1]:
                for j in range(len(nums) - 1, i, -1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j], nums[i]
                        break
                        # can't use nums[i+1:].reverse() to swap
                for j in range(0, (len(nums) - i) // 2):
                    nums[0 + j + (i + 1)], nums[len(nums) - 1 - (i + 1) - j + (i + 1)] = nums[len(nums) - 1 - (
                    i + 1) - j + (i + 1)], nums[0 + j + (i + 1)]
                break
        else:
            nums.reverse()


if __name__ == "__main__":
    answer=Solution()
    print answer.nextPermutation([1,3,2])


# 6 5 4 8 7 5 1
#首先肯定从后面开始看,1和5调换了没有用。
#7、5和1调换了也没有效果,因此而发现了8、7、5、1是递减的。
#如果想要找到下一个排列,找到递增的位置是关键。
#因为在这里才可以使其增长得更大。
#于是找到4了,显而易见4过了是5而不是8或者7更不是1。
#因此就需要找出比4大但在这些大数里面最小的值,并将其两者调换。
#那么整个排列就成了:6 5 5 8 7 4 1
#然而最后一步将后面的8 7 4 1做一个递增。

# public class Solution {
#     public static int[] nextPermutation(int[] nums) {
#         int i, j, temp, len=nums.length;
# 		for(i=len-1-1; i>=0; i--){
# 			if(nums[i]<nums[i+1]){
# 				for(j=len-1; j>i; j--){
# 					if(nums[i]<nums[j]){
# 						temp=nums[j];
# 						nums[j]=nums[i];
# 						nums[i]=temp;
# 						break;
# 					}
# 				}
# 				for(j=i+1;j<i+1+(len-(i+1))/2;j++){
# 					temp=nums[j];
# 					nums[j]=nums[(len-1-i)-(j-(i+1))+i];
# 					nums[(len-1-i)-(j-(i+1))+i]=temp;
# 				}
# 			}
# 		}
# 		return nums;
#     }
#
# 	public static void main(String[] args){
# 		Solution answer = new Solution();
# 		int[] returnList = answer.nextPermutation(new int[]{6, 5, 4, 8, 7, 5, 1});
# 		for(int i = 0; i < returnList.length; i++){
# 			System.out.print(" "+ returnList[i]);
# 		}
# 	}
# }