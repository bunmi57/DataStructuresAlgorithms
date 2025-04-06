'''
You are given an integer array height of length n. 
There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.

Hint:
- use a 2 pointer appreach 
- 1 pointer at start, 1 pointer at end 
- move pointer that's at shorter line
'''

def maxArea(height):
    i = 0
    j = len(height)-1
    #edge case 
    if len(height) < 2:
        return height
    #Area = length x breadth
    max_area = min(height[i], height[j]) * (j-i)
    while i < len(height) and j > -1:
        #move the pointer that's at the shorter line, because the area is limited by the shorter height
        if height[i] < height[j]:
            i += 1
        else:
            j -= 1
        #find the area 
        current_area = min(height[i], height[j]) * (j-i)
        print('Current Area:',current_area)
        #update/keep max area
        max_area = max(max_area, current_area)
        print('in function Max Area:',max_area)

    return max_area

# height = [1,8,6,2,5,4,8,3,7]
height = [5,9,2,1,4]
print('\nMax Area:', maxArea(height))