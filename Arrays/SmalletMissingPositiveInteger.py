'''
Find the smallest missing positive integer
1.Check if all numbers are negative or zero:if yes return 1
2.Remove all non-positive numbers (negative numbers and zero):
3. Sort the remaining positive numbers in ascending order:
4. Loop through the sorted array
'''
new_array = []
arr1 = [3,4,-1,-1,1,1] #2
arr2 = [1,2,0] #3
arr3 = [7,8,9,10,11] #1
arr4 = [2,3,4,5,6,7,8,9,10,12] #1
def missingPositiveInteger(arr):
    #Remove all non-positive numbers (negative numbers and zero)
    for num in arr:
        if num > 0: 
            new_array.append(num)

    #sort the positive numbers in ascending order
    sorted_array = sorted(new_array)
    
    #If sorted array is empty,for example having all negative numbers return 1
    if sorted_array == []: #if not sorted_array
        return 1
        
    print(f"Sorted array: {sorted_array}")

    #Loop through the positive array to find the mising number
    start = sorted_array[0]
    i = 0
    for j in range(1,len(sorted_array)):
        if sorted_array[j] - sorted_array[i] != 1: #if the difference between the next element and the present element is not equal to 1
            return sorted_array[i] + 1 #Add 1 to the present element 
        i += 1

    
    if start == 1:
        return sorted_array[-1] + 1 #return last index + 1

    return 1

print(missingPositiveInteger(arr4))
