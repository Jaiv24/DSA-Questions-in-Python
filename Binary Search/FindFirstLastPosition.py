# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1, -1]
        def search(nums, target, findStartIndex: bool):
            ans = -1 
            start = 0
            end = len(nums) - 1 

            while start <= end:
                mid = start + (end - start) // 2

                if nums[mid] < target:
                    start = mid + 1               
                elif nums[mid] > target:
                    end = mid - 1 

                else:
                    ans = mid
                    if findStartIndex is True:
                        end = mid - 1
                    else:
                        start = mid + 1

            return ans

        start = search(nums, target, True)
        end = search(nums, target, False)

        ans[0], ans[1] = start, end
        return ans