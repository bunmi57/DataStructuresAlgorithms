'''
You are given an integer array nums and two integers indexDiff and valueDiff.

Find a pair of indices (i, j) such that:

i != j,
abs(i - j) <= indexDiff.
abs(nums[i] - nums[j]) <= valueDiff, and
Return true if such pair exists or false otherwise.
'''
def containsDuplicateIII(nums,indexDiff, valueDiff):
    left = 0
    while left < len(nums)-1:
        print(f"Left: {left}")
        for right in range(left+1,len(nums)):
            print(f"Right : {right}")
            if left != right and abs(left-right) <= indexDiff and abs(nums[left]-nums[right]) <= valueDiff:
                return True
        left += 1
    return False

nums = [1,2,3,1]
indexDiff = 3
valueDiff = 0
print(containsDuplicateIII(nums,indexDiff,valueDiff))


