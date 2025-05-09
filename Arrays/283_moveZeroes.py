'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

'''
def moveZeroes(nums):
    # #first attempt - incorrect for nums = [0,0,1]
    # #find the length of nums
    # length = len(nums)

    # #loop through the length of the array
    # for i in range(length):
    #     #if zero, pop and append
    #     if nums[i] == 0:
    #         popped = nums.pop(i)
    #         nums.append(popped)

    # return nums

    #Another soln
    left = 0
    #find the length of nums
    length = len(nums)

    #iterate through the array 
    for _ in range(length):
        if nums[left] == 0:
            popped = nums.pop(left)
            nums.append(popped)
        else: #non-zero, move left forward
            left += 1
    return nums

print(moveZeroes(nums = [0,0,0, 4,6,0,9]))