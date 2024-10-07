
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        count = len(nums)
        for i, n in enumerate(nums):
            if i >= count-1:
                break
            while n == nums[i+1]:
                nums.pop(i)
                nums.append('_')
                count -= 1
        return count

l = [1, 2, 3, 4, 5]
l = [0, 0, 1, 1, 1, 1, 1, 2, 2, 3, 3, 4]
print(l)

o = Solution()
r = o.removeDuplicates(l)
print(r)
print(l)
