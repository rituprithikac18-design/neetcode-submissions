class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        lsum=rsum=maxsum=0
        n=len(cardPoints)
        for i in range(k):
            lsum+=cardPoints[i]
        maxsum=lsum
        rindex=n-1
        for i in range(k-1,-1,-1):
            lsum-=cardPoints[i]
            rsum+=cardPoints[rindex]
            maxsum=max(maxsum,lsum+rsum)
            rindex-=1
        return maxsum