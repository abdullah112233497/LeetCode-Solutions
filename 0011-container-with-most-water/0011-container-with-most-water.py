class Solution:
    def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        max_a=0
        while l<r:
            
            area=(r-l)*min(height[r],height[l])
            max_a=max(max_a,area)
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return max_a
            
            
        