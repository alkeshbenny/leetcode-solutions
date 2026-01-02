class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n  # Handle k > n
        
        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        # Step 1: Reverse entire array
        reverse(nums, 0, n-1)
        
        # Step 2: Reverse first k elements
        reverse(nums, 0, k-1)
        
        # Step 3: Reverse remaining elements
        reverse(nums, k, n-1)
