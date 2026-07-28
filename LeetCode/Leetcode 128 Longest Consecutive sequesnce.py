nums = [1,99,101,98,2,6,3,100,101,4,102,97,1,2,1]

#Bruteforce
def LongestConsecSequence(nums):
    nums = sorted(list(set(nums)))
    longseq = 0 
    curr_seq =1

    for i in range(len(nums)-1):
        if nums[i+1] == nums[i]+1:
            curr_seq += 1
        else:
            longseq = max(longseq,curr_seq)
            curr_seq = 1
    longseq = max(longseq,curr_seq)
    return longseq

print(LongestConsecSequence(nums))

"""Time Complexity : O(nlog(n)) 
   Space complexity : O(n)"""
   
nums = [1,99,101,98,2,6,3,100,101,4,102,97,1,2,1]

#Optimized
def longestConsecutiveSet(nums):
    if not nums:
        return 0
    num_set = set(nums)  
    long_streak = 0  
    for num in num_set:
        if num - 1 not in num_set:
            curr_num = num
            curr_streak = 1
            while curr_num + 1 in num_set:
                curr_num += 1
                curr_streak += 1
            long_streak = max(long_streak, curr_streak)
    return long_streak

print(longestConsecutiveSet(nums))

"""Time Complexity : O(n) 
   Space complexity : O(n)"""