'''
Given a binary array nums and an integer k,
return the maximum number of consecutive 1's in the array if you can flip at most k 0's.


'''
def longestOnes(nums,k):
    left = 0
    right = 1
    index = 0

    count_zero = 0
    count_one = 0
    max_ones = 0
    #left
    if nums[left] == 0:
        count_zero += 1
    else:
        count_one += 1

    #loop through nums until the end, and as long as number of 0 is not equal to k
    #while right < len(nums) and count_zero < k:
    while right < len(nums):
        #right
        index += 1
        if nums[right] == 0:
            count_zero += 1
        else:
            count_one += 1
        #calculate number of ones
        while count_zero > k:
            current_ones = count_one + k
            max_ones = max(max_ones,current_ones)
            if nums[left] == 1:
                count_one -= 1
            else: #if nums[left] is 0
                count_zero -= 1
        #move right 
        print(f'index:{index}, right:{right}, max:{max_ones}')
        right += 1

    return max_ones



print("Output is 6:",longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))
# print("Output is 10:",longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],3))