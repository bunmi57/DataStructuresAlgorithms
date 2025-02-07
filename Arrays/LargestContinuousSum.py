'''
Given an array of integers (positive and negative)
Find the largest continuous sum
Return sum, start of the sum and end of the sum

'''
arr1 = [1,2,-1,3,4,10,10,-10,-1] #largest continuous sum is 29
arr2 = [1,2,-1,3,4,-1] #largest continuous sum is 9
arr3 = [-2, -3, 4, -1, -2, 1, 5, -3]
arr4 = [3, -2, 5, -1, 6, -3, 2, 7, -5, 2]
arr5 = [10, -3, 2, 1, -5, 4, 6, -2, 8, -10, 3, 5]
arr6 = [-1, -2, -3, -4]
arr7 = [1, 2, 3, 4, 5]
arr8 = [5, -1, -2, 3, -1, 2, 4, -3, 6]
arr9 = [2, -8, 3, 5, -2, 4, -10, 6, 7]
arr10 = [1, -2, 3, 4, -1, 2, 1, -5, 4]


def largestSum(arr):
    sum_total = arr[0]
    largest_sum= {}
    for i in range(1,len(arr)):
        sum_total += arr[i]
        #print(f"Sumtotal at {i} = {sum_total}")
        if sum_total < sum_total - arr[i]: #if present sum is less than previous sum
            largest_sum[i-1] = sum_total - arr[i] #store the last largest sum and the stop index 
    print(f"Largest continuous sum: {max(largest_sum.values())}") #find the largest value in the dictionay 
    for key,value in largest_sum.items():
        if value == max(largest_sum.values()):
            #return (max(largest_sum.values()),key)
            print(f"Stop index: {key}")
    
