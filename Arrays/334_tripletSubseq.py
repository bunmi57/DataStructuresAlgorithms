'''
Given an integer array nums, 
return true if there exists a triple of indices (i, j, k) 
such that i < j < k and nums[i] < nums[j] < nums[k].
 If no such indices exists, return false.
'''
nums = [2,1,5,0,4,6]
def triplet(nums):
    #initialize i and j to large values
    i = float('inf')
    j = float('inf')

    #iterate through the array 
    for num in nums:
        if num <= i:
            i = num #replace i so that it is the smallest value  
        elif num <= j:
            j = num # num is bigger than i but smaller than j
        else:
            # Found a number bigger than both i and j → triplet exists
            return True
    
    return False
print(triplet(nums))


