'''
You are given an array of integers nums, there is a sliding window of size k 
which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. 
Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]

Steps
1. Initialize output list, left = 0
2. Loop through the array len(nums)-k+1 times
3. Find the max value in the window from left (index 0) to right (k-1)
4. Append the max value to the list 
5. Move left index by 1 and right index by 1
6. repeat steps 3-5
7. Edge cases:
    if list is empty, return empty list 
    if list has 1 element and k = 1, return element
    if length of list < k, return empty list
'''
# def slidingWindowMaximum(nums,k):
#     #Initialize output list, left = 0
#     left = 0
#     output = []
#     #if list is empty or len of list is less than k, return empty list 
#     if not nums or len(nums) < k:
#         return []
#     #if list has 1 element and k = 1, return element
#     if len(nums) == 1 and k == 1:
#         return nums
#     #loop through the array 
#     for right in range(left+k-1,len(nums)):
#         output.append(max(nums[left],nums[left+1],nums[right]))
#         left += 1
#     return output

def slidingWindowMaximum(nums,k):
    #if the list is empty , or k is zero or length of the list is smaller than k
    if not nums or k == 0 or len(nums)<k:
        return []
    #if the list has 1 element and k = 1, return the element
    if len(nums) == 1 and k == 1:
        return nums
    output = []
    #loop through the array using a sliding window
    for left in range(len(nums)-k+1):
        output.append(max(nums[left:left+k])) #find the max in the window
    
    return output
nums = [1,3,-1,-3,5,3,6,7]
# nums = []
k = 4
print(slidingWindowMaximum(nums,k))    