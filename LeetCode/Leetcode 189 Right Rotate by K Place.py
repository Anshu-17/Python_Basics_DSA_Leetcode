nums = [3, 9, 5, 6,7, 2]
k = 3
#Brute Force Approach
def rotatebyK_BF(nums, k):
    n = len(nums)
    rm = k % n
    for _ in range(rm):
        last = nums.pop()
        nums.insert(0, last)
        
''' Time Complexity: O(n*k) where n is the length of the array and k is the number of rotations.
    Space Complexity: O(1) as we are not using any extra space.'''
    
print("Before Rotation_BF:", nums)
rotatebyK_BF(nums, k)
print("After Rotation_BF:", nums)
    
# Optimal Approach
def rotatebyK_Optimal(nums, k):
    n = len(nums)
    rm = k % n
    nums[:] = nums[-rm:] + nums[:-rm]
    
''' Time Complexity: O(n) where n is the length of the array.
    Space Complexity: O(1) as we are not using any extra space.'''
    
print("Before Rotation_Optimal:", nums)
rotatebyK_Optimal(nums, k)  
print("After Rotation_Optimal:", nums)


# Without using Slicing
def rotatebyK_WithoutSlicing(nums, k):
    n = len(nums)
    rm = k % n
    nums.reverse()
    nums[:rm] = reversed(nums[:rm])
    nums[rm:] = reversed(nums[rm:])
    
''' Time Complexity: O(n) where n is the length of the array.
    Space Complexity: O(1) as we are not using any extra space.'''
    
print("Before Rotation_WithoutSlicing:", nums)
rotatebyK_WithoutSlicing(nums, k)
print("After Rotation_WithoutSlicing:", nums)