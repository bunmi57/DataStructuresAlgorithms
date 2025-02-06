'''
Consider an array of non-negative integers. 
A second array is formed by shuffling the elements of the first array and
deleting a random element. Given these two arrays, find which element is missing in the
second array.

Here is an example input, the first array is shuffled and the number 5 is removed to construct the second array.

Input:

finder([1,2,3,4,5,6,7],[3,7,2,1,4,6])
Output:

5 is the missing number

'''
arr1 = [1,2,3,4,5,6,7]
arr2 = [3,7,2,1,4,6]

#initilaize a new array 

# def missingElement(arr1,arr2):
#     new_dict = {}
#     #Loop throug arr1, and count the occurence
#     for num in arr1:
#         if num not in new_dict:
#             new_dict[num] = arr1.count(num)
#     print(new_dict)
#     for num in arr2:
#         if new_dict[num] < arr2.count(num):
#             print(f"{num} is missing")
# print(missingElement(arr1,arr2))


#------------------------Another solution----------------------------------------
# def missingElement(arr1, arr2):
#     # Initialize a dictionary to store the count of numbers in arr1
#     new_dict = {}

#     # Populate the dictionary with counts from arr1
#     for num in arr1:
#         new_dict[num] = new_dict.get(num, 0) + 1

#     # Reduce the count for numbers found in arr2
#     for num in arr2:
#         if num in new_dict:
#             new_dict[num] -= 1

#     # Find the missing number (the one with count > 0)
#     for num, count in new_dict.items():
#         if count > 0:
#             return f"{num} is the missing number"

#     return "No missing number found"

# Test case
# arr1 = [1, 2, 3, 4, 5, 6, 7]
# arr2 = [3, 7, 2, 1, 4, 6]
# print(missingElement(arr1, arr2))  # Output: "5 is the missing number"

#-----------------------Third solution------------------------------------------
arr1 = [1, 2, 3, 4, 5, 6, 7]
arr2 = [3, 7, 2, 1, 4, 6]
import collections
def finder2(arr1,arr2):
    d = collections.defaultdict(int) #prevents keyerror

    for num in arr2:
        d[num] += 1
        print(d)
    for num in arr1:
        if d[num] == 0:
            print(f"if d reduction: {d}")
            return num
        else:
            d[num] -= 1
            print(f"else d reduction: {d}")

print(finder2(arr1,arr2))