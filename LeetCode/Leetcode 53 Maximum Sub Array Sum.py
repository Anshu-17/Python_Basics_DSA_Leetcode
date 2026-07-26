nums = [-2,1,-3,4,-1,2,1,-5,4]

# Brute Force Approach
def maxSubArray(nums):
    max_sum = float('-inf')
    n = len(nums)
    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += nums[j]
            max_sum = max(max_sum, current_sum)
    return max_sum

print(maxSubArray(nums)) 

'''Time Complexity: O(n^2)
Space Complexity: O(1)'''

# Optimized Approach (Kadane's Algorithm)
def maxSubArrayOptimized(nums):
    max_sum = curr_sum = nums[0]
    for num in nums[1:]:
        curr_sum =  max(num, curr_sum + num)
        max_sum = max(max_sum, curr_sum)
    return max_sum
print(maxSubArrayOptimized(nums))

'''Time Complexity: O(n)
Space Complexity: O(1)'''