class Solution:
    def FindPythagoreanTriplets(self,nums):
        for a in nums:
            for b in nums:
                for c in nums:
                    if a*a + b*b == c*c:
                        return True
        return False

    def FindPythagoreanTriplets2(self, nums):
        squares = set([n*n for n in nums])

        for a in nums:
            for b in nums:
                if a*a + b*b in squares:
                    return True
        return False


nums = [3, 5, 12, 5, 13] #True
nums2 = [3, 5, 17, 5,13] #False
print (Solution().FindPythagoreanTriplets2(nums))
print (Solution().FindPythagoreanTriplets2(nums2))

