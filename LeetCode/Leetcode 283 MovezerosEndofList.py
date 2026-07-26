nums = [0,1,0,0,6,0,2,4,0,7,0]

#Brute Force Approach
def moveZeroes(nums):
    n = len(nums)
    i = 0
    while i < n:
        if nums[i] == 0:
            nums.append(nums.pop(i))
            n -= 1
        else:
            i += 1
            
'''Time Complexity: O(n^2) where n is the length of the array.
Space Complexity: O(1) as we are not using any extra space.'''

print("Before MoveZeroes:", nums)
moveZeroes(nums)
print("After MoveZeroes:", nums)

#Using Sort Function
nums = [0,1,0,0,6,0,2,4,0,7,0]

def moveZeroesSort(nums):
    nums.sort(key=lambda x: x == 0)

'''Time Complexity: O(nlogn) where n is the length of the array.
Space Complexity: O(1) as we are not using any extra space.'''

print("Before MoveZeroesSort:", nums)
moveZeroesSort(nums)
print("After MoveZeroesSort:", nums)

#Optimal Approach - Two Pointer Approach
nums = [0,1,0,0,6,0,2,4,0,7,0]

def moveZeroesTwoPointer(nums):
    n =len(nums)
    left = 0 
    for right in range(n):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left +=1
            
'''Time Complexity: O(n) where n is the length of the array.
Space Complexity: O(1) as we are not using any extra space.'''

print("Before MoveZeroesTwoPointer:", nums)
moveZeroesTwoPointer(nums)  
print("After MoveZeroesTwoPointer:", nums)