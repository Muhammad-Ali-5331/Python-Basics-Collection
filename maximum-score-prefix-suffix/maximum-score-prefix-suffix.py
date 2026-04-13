class Solution:
    def maximumScore(self, nums) -> int:
        prefix = [nums[0]]
        for i in range(1,len(nums)): prefix.append(nums[i] + prefix[i-1])
        suffix = [nums[-1]]
        for i in range(len(nums)-1,-1,-1): suffix.append(min(nums[i],suffix[-1]))
        suffix = suffix[::-1]
        mx = float('-inf')
        for i in range(len(prefix)-1): mx = max(prefix[i]-suffix[i+1],mx)
        return mx

obj = Solution()
arr = [-7,-5]
print(obj.maximumScore(arr))