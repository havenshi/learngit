# -*- coding: utf-8 -*-
# track两个index，一个是red的index，一个是blue的index，两边往中间走。
# i从0到blue index扫描，
# 遇到0，放在red index位置，red index后移；
# 遇到2，放在blue index位置，blue index前移；
# 遇到1，i后移。
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        red, blue = 0, len(nums)-1   # red means position which should be 0; blue means position which should be 2.
        i = 0
        while i < blue + 1:
            if nums[i] == 0:
                nums[i], nums[red] = nums[red], nums[i]
                red += 1    # red index move forward
                i += 1      # i move forward
            elif nums[i] == 2:
                nums[i], nums[blue] = nums[blue], nums[i]
                blue -= 1   # blue index move forward.
                # don't move i! since now nums[i] could be 0(smaller than the item before it) or 1, this item needs to be judged again.
            else:
                i += 1
