'''
Find the length of smallest contifuous subarray whose sum is >= s
1 Set Up the Basics

Start with a window that covers no elements (left = 0).
Keep track of the sum of the elements inside the window.
Keep a variable to store the smallest subarray length found.
2️ Expand the Window

Move right across the array, adding each element to the sum.
This grows the window until the sum is at least S.
3️ Shrink the Window to Find the Shortest Length

If the sum reaches or exceeds S, try to shrink the window by moving left forward.
Each time you shrink, check if the new window is smaller than the previous smallest one.
4️ Continue Until the End of the Array

Keep repeating steps 2 & 3 until you’ve checked all possible windows.
5️ Return the Smallest Length

If no valid subarray was found, return 0 (meaning no solution).

arr = [2,3,1,2,4,3] s = 7
'''
def smallestContinuousArray(arr,s):
    #initialize the variables
    left = 0
    sum_elements = 0
    min_subarray_length = 0
    min_length = float('inf')

    #expand the window , move right across the array,adding each element to the sum
    for right in range(len(arr)):
        sum_elements += arr[right]
        print(f"right = {right} sum = {sum_elements} left = {left}")

        #shrink the window to find the shortest length 
        while sum_elements >= s:
            #shrink the window to the left
            sum_elements -= arr[left]
            print(f"shrunk sum = {sum_elements}, right = {right}")

            #find the smallest length
            min_length = min(min_length,right -left+1)
            print(f"Min length = {min_length}")

            left += 1
            print(f"new Left = {left}")

            print('\n')
    if min_length == float('inf'):
        return 0
    else:
        return min_length
# arr = [2,3,1,2,4,3] 
#      0,1,2,3,4,5
# s = 7
arr = [1,1,1,1,1,1,1,1,5,1]
s = 11
print(smallestContinuousArray(arr, s))

