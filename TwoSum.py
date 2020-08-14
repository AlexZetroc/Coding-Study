class Solution(object):
        
    def TwoSumA(self, nums, target):
        for i1, a in enumerate(nums):
            for i2, b in enumerate(nums):
                if a == b:
                    continue
                if a + b == target: 
                    return[i1,i2]

    def TwoSumB(self, nums, target):
        values = {}
        for i, num in enumerate(nums):
            diff = target - num

            if diff in values:
                return [i, values[diff]]
            values[num] = i
        return []


print(Solution().TwoSumA([2,7,11,15], 18))
print(Solution().TwoSumB([2,7,11,15], 18))