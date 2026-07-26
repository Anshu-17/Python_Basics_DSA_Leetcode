nums = [3, 1, -2, -5, 2, -4]

# Brute Force Approach
def rearrange_array(nums):
    pos = []
    neg = []
    for i in nums:
        if i>=0:
            pos.append(i)
        else:
            neg.append(i)
    for j in range(len(pos)):
        nums[2*j] = pos[j]
        nums[2*j + 1] = neg[j]
    return nums

print(rearrange_array(nums))

'''time complexity: O(n)
space complexity: O(n)'''

nums = [3, 1, -2, -5, 2, -4]

# Optimal Approach
def rearrange_array_optimal(nums):
    n= len(nums)
    result = [0]*n #o(n)
    pos_index , neg_index = 0, 1
    for i in range(n):
        if nums[i]>=0:
            result[pos_index] = nums[i]
            pos_index += 2
        else:
            result[neg_index] = nums[i]
            neg_index += 2
    return result

print(rearrange_array_optimal(nums))
'''time complexity: O(n)
space complexity: O(n)'''