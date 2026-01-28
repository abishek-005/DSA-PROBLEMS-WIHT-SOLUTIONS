#Area = min(height[left], height[right]) × (right - left)
class Solution:
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        max_area = 0

        while l < r:
            h = min(height[l], height[r])
            w = r - l
            max_area = max(max_area, h * w)

            # move the pointer with smaller height
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
