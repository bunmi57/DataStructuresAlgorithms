'''
Given an integer array nums and an integer val, 
remove all occurrences of val in nums in-place. 
The order of the elements may be changed. 
Then return the number of elements in nums which are not equal to val.
'''
class Solution(object):
    def removeElement(self, nums, val):
        count = 0
        val_index = []
        #loop through array 
        for i in range(len(nums)):
            #if element is val, store index
            if nums[i] == val:
                val_index.append(i)
            else:
                count += 1 #count element that is = to val 
                #replace position of element with position of val
                if len(val_index) >= 1:
                    nums[val_index[0]] = nums[i]
                    val_index.pop(0)
                    #add position of moved variable
                    val_index.append(i)
        return count,nums
    

nums = [0,1,2,2,3,0,4,2]
val = 2
sol = Solution()
print(sol.removeElement(nums, val))
