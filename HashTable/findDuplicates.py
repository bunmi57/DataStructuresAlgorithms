'''
Problem: Given an array of integers nums, 
find all the duplicates in the array using a hash table (dictionary)

steps
- for each element in the list
- check if element is in dict
    if not, add with count of 1
    if in dict, inc count by 1
    if count > 1, add to output list
'''
def find_duplicates(nums):
    #initialize input dict
    input_dict = {}
    output = []
    #for each element in the list, add in dictionary 
    if len(nums) == 0:#for empty list 
        return []
    #Add each element to the dict
    for element in nums:
        if element in input_dict:
            count = input_dict[element] + 1
            if count > 1 and element not in output:#avoid adding duplicate elements multiple times, use set instead and add
                output.append(element)
        else:
            input_dict[element] = 1
    
    return output
print ( find_duplicates([1, 2, 3, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 3]) )
print ( find_duplicates([1, 1, 1, 1, 1]) )
print ( find_duplicates([1, 2, 3, 3, 3, 4, 4, 5]) )
print ( find_duplicates([1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([1, 1, 1, 2, 2, 2, 3, 3, 3, 3]) )
print ( find_duplicates([]) )