import unittest

def twoSum(nums, target):
    m = {}
    for i in range(len(nums)):
        if nums[i] in m:
            return [m[nums[i]], i]
        else:
            m[target - nums[i]] = i
    return m

class TestMyfuntions(unittest.TestCase):
    def test1(self):
        self.assertTrue(twoSum([1,2,3], 4))

    def test2(self):
        self.assertTrue(twoSum([2,2,4,4], 6))

if __name__ == '__main__':
    unittest.main(exit=False)