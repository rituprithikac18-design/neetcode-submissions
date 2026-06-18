class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currsum=maxsum=nums[0]
        for i in range(1,len(nums)):
            currsum=max(currsum+nums[i],nums[i])
            maxsum=max(currsum,maxsum)
        return maxsum