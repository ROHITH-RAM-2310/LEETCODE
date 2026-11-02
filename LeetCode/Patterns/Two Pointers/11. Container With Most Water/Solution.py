class Solution:
    def maxArea(self, height: list[int]) -> int:
        lef = 0
        rig = len(height)-1
        ans = 0
        while lef < rig :

            h = min(height[lef],height[rig])
            w = rig - lef
            
            ans = max(ans,h*w)

            if height[lef] < height[rig] :
                lef = lef + 1
            else :
                rig = rig - 1
        return ans