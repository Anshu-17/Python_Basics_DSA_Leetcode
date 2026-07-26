Nums = [4,6,7,11,2,1,3,5,8,9]
target = 1

def twosum(nums,target):
    num_dict = {}
    for i ,num in enumerate(nums):
        diff = target - num
        if diff in num_dict:
            return [num_dict[diff],i]
        num_dict[num] = i
    return []
result = twosum(Nums,target)
print(result)