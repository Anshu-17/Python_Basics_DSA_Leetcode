Nums = [1,1,0,1,1,1,0,0,1,1,1,1,0,1]

def findMaxConsecutiveOnes(nums):
    max_count = 0
    current_count = 0 
    for i in nums:
        if i ==1:
            current_count += 1
            max_count = max(max_count, current_count)
        else:            
            current_count = 0
    return max_count

print(findMaxConsecutiveOnes(Nums))
        