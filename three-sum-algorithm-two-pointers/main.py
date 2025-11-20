class Solution:
    def threeSum(self, nums):
        res = list()
        nums.sort()
        for i,n in enumerate(nums):
            left,right = i+1,len(nums)-1
            while left < right:
                s = n + nums[left] + nums[right] 
                if s == 0:
                    res.append([n,nums[left],nums[right]])
                    left+=1
                    while nums[left] == nums[left-1] and left < right: left+=1
                elif s < 0:
                    left+=1
                else:
                    right-=1
        return res

obj = Solution()

arr = [-2,0,1,1,2]

print(obj.threeSum(arr))