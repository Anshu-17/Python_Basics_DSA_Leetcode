Nums = [9,2,1,4,6,8,3,5,0]
def missingNumber(nums):
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)
missing = missingNumber(Nums)
print(missing)