'''
You are given an integer array nums and an integer k.
In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
Return the maximum number of operations you can perform on the array.

 
Example 1:
Input: nums = [1,2,3,4], k = 5
Output: 2

Example 2:
Input: nums = [3,1,3,4,3], k = 6
Output: 1

'''

def maxOperations(nums,k):
    #use 2 pointer approach 
    left = 0
    right = len(nums)-1
    count = 0

    #sort array 
    sorted_nums = sorted(nums)

    
    while left < right:
        sum = sorted_nums[left] + sorted_nums[right]
        if sum > k:
            right -= 1
        elif sum == k:
            count += 1
            left += 1
            right -= 1
        else:#sum < k
            left += 1

    return count

print(maxOperations(nums = [3,1,3,4,3], k = 6))