class Solution:
    def trap(self, height: List[int]) -> int:
        rightMaxArray = [0]*len(height)
        curRightMax = height[-1]
        for i in range(len(height)-2, -1, -1):
            rightMaxArray[i] = max(height[i+1], rightMaxArray[i+1])
            
        res = 0
        curLeftMax = height[0]
        for i in range(1,len(height)):
            curLeftMax = max(height[i-1], curLeftMax)
            curRes = min(curLeftMax, rightMaxArray[i]) 
            if curRes > height[i]:
                res += curRes - height[i]
            
        return res
