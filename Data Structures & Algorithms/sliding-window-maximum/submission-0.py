class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxSum=[]

        l,r=0,k-1
        while r<len(nums):
            maxi=nums[l]
            for i in  range(l,r+1):
                maxi=max(maxi,nums[i])
            l+=1
            r+=1
            maxSum.append(maxi)
        return maxSum
        