'''
You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's,
where 0 means empty and 1 means not empty, and an integer n,
return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

*************** **************** ***************

Question 1: What determines if you can plant new flowers? 

* Need a zero
* Do not want a 1 next to the zero on the left or right 

Question 2: How do we know where we can plant new flowers (flower_count) - we know when two conditions are met 

2. When you see zero 
3. Then check for left and right of the  zero and make sure there is no 1  - if there is no left then check only right. If there is no right then check only left.
* If left is 0 - we can plant
* If right is 0 - we can plant 
* If left is 0 but right is 1 - we can not plant 
* If left is 1 but  right is 0- we can not plant 
* If left is 0 and right is 0 - we can plant 
* If left is 1 and right is 1 - we can not plant
* If no left, right is not 1 - we can plant 

   3. What happens next : 
* If we can plant: add 1 to flower_count. 
* Replace the zero by 1 



001
100
000
101


*************** **************** ***************

1. Need to know where the zeros are relative to the ones? If a zero is next to 1 you can’t add a flower 
2. Want to count the number of new flowers and compare to n?
3. If count is = n at any point.  Return True 
4. Finally return false 

*************** **************** ***************
Pseudo code - check if flower can be planted 
2. Check if number is 0 
3. Check the value to the left and right 
4. Determined if we can plant 
5. If we can plant: add 1 to flower_count. 
6. Replace the zero by 1 in the array 

*************** **************** ***************
Pseudo code - entire code 
1. Check if flower can be planted 
2. Compare no of new flowers to n 
3. If new flowers is equal or greater than n , return true 
4. Continue to loop
5. Once loop is completed, return false 


input: flowerbed, n
output: True or False
Goal: return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise

*************** **************** ***************
Pseudo code - check if flower can be planted 
2. Check if number is 0 
3. Check the value to the left and right 
4. Determined if we can plant 
5. If we can plant: add 1 to flower_count. 
6. Replace the zero by 1 in the array 
'''

flowerbed = [1,0,0,0,1,0,0]
n = 2
#first attempt 
# def canPlaceFlowers(flowerbed,n):
#     #initialize flower_count
#     flower_count = 0
#     #if 001
#     in_test = [0,0,1]
#     if flowerbed[0:3] == in_test:
#         flower_count += 1
#     #check if flower can be plantedithout violating the no-adjacent-flowers rule
#     for i in range(1,len(flowerbed)):
#         #Check if number is 0 
#         if flowerbed[i] == 0 and flowerbed[i+1] != 1:
#             #Check the value to the left and right 
#             if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:#If left is 0 and right is 0 - we can plant 
#                 #If we can plant: add 1 to flower_count. 
#                 flower_count += 1
#                 #Replace the zero by 1 in the array 
#                 flowerbed[i] = 1
#             if flowerbed[i-1] == 0 and flowerbed[i+1] == 1 :#If left is 0 and right is 1 - we can plant 
#                 #If we can plant: add 1 to flower_count. 
#                 flower_count += 1
#                 #Replace the zero by 1 in the array 
#                 flowerbed[i] = 1
#         #Compare no of new flowers to n, If new flowers is equal t0 n , return true 
#         if flower_count == n:
#             return True 
#     #Once loop is completed, return false 
#     return False

def canPlaceFlowers(flowerbed,n):
    #initialize flower_count
    flower_count = 0
    length = len(flowerbed)

    for i in range(length):
        #check if current plot is empty
        if flowerbed[i] == 0:
            #check left and righr neighbours (handles edges safely)
            empty_left = (i==0) or (flowerbed[i-1]==0) #i = 0, checks if a plot is on the edge and has no left neighbour
            empty_right = (i==length-1) or (flowerbed[i+1]==0) #if length - 1 is checked first If i == length - 1, you hit flowerbed[i + 1] first, 
                                                               #which causes an IndexError because you're accessing out of bounds before checking the safe condition
                                                               #i is the last index, i == length - 1 evaluates to True

            if empty_left and empty_right:
                #plant flower
                flowerbed[i] = 1
                flower_count += 1

                if flower_count >= n:
                    return True
    return flower_count >= n
print(canPlaceFlowers(flowerbed,n)) #expected - true

                

