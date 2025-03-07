'''
We are given an array asteroids of integers representing asteroids in a row. 
The indices of the asteriod in the array represent their relative position in space.
For each asteroid, the absolute value represents its size, and
the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.
Find out the state of the asteroids after all collisions. 
If two asteroids meet, the smaller one will explode. 
If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.
Example 1:
Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:
Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:
Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
Steps 
- while true
-   pop top of the stack, initialize as "popped" 
-   peak stack, initilaize as "peaked" 
    if pop and peak exist (i.e there are at least 2 values to compare)
-       compare pop and peak 
    -   if opposite sign #not the same direction(can meet), so 1 positive, 1 negative
            if same size, both explode
                remove peaked # exploding the 2 asteroids(popped and peak)
            else #oppsite sign but different size, smaller explode
                if smaller is popped value, do nothing 
                if smaller is peaked value, you want to pop peaked and return popped to stack
    -   else #same size, 2 posive, or 2 negative , cannot meet
            return poped value to stack 
-  return stack 
- edge case (addressed above)- if only one value or 0 in stack, return the stack
'''
# class Solution(object):
#     def asteroidCollision(self, asteroids):
#         while len(asteroids) >= 2:
#             if len(asteroids) == 2:
#                 popped = asteroids.pop()
#                 peaked = asteroids[0]
#                 if (peaked < 0 and popped > 0) or (peaked > 0 and popped < 0): #opposite sign 
#                     #if same size, both explode
#                     if abs(peaked) == abs(popped):
#                         asteroids.remove(peaked) #remove peaked, exploding the 2 asteroids(popped and peak)
#                     #else #oppsite sign but different size, smaller explode
#                     else:
#                         if abs(peaked) < abs(popped):
#                             asteroids.remove(peaked)
#                             asteroids.append(popped)
#                         #if smaller is popped value, do nothing 
#                 else:
#                     #same size, 2 posive, or 2 negative , cannot meet,return poped value to stack 
#                     asteroids.append(popped)
#                 return asteroids

#             else:
#                 #pop top of the stack, initialize as "popped" 
#                 popped = asteroids.pop()
#                 #peak stack, initilaize as "peaked" 
#                 peaked = asteroids[-1]
#                 if (peaked < 0 and popped > 0) or (peaked > 0 and popped < 0): #opposite sign 
#                 #if same size, both explode
#                     if abs(peaked) == abs(popped):
#                         asteroids.remove(peaked) #remove peaked, exploding the 2 asteroids(popped and peak)
#                     #else #oppsite sign but different size, smaller explode
#                     else:
#                         if abs(peaked) < abs(popped):
#                             asteroids.remove(peaked)
#                             asteroids.append(popped)
#                         #if smaller is popped value, do nothing 
#                 else:
#                     #same size, 2 posive, or 2 negative , cannot meet,return poped value to stack 
#                     asteroids.append(popped)

#         return asteroids #return stack
#Solution 1
class Solution(object):  
    def asteroidCollision(self,asteroids):
        while len(asteroids)>= 2:
            popped = asteroids.pop()
            if asteroids:#not empty
                peaked = asteroids[-1]
            else:
                None
            if peaked is not None and (peaked<0<popped or peaked>0>popped ):
                if abs(peaked)== abs(popped):
                    asteroids.pop()
                elif abs(peaked)<abs(popped):
                    asteroids.pop()
                    asteroids.append(popped)
            else:
                asteroids.append(popped)
        return asteroids
#solution 2
class Solution(object):
    def asteroidCollision(self, asteroids):
        stack = []  # Using a separate stack instead of modifying the input list

        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:  # Only collide if opposite signs
                top = stack[-1]
                if abs(top) < abs(asteroid):  
                    stack.pop()  # Top explodes, continue checking for more collisions
                elif abs(top) == abs(asteroid):
                    stack.pop()  # Both explode
                    break  # No need to add asteroid
                else:
                    break  # Smaller asteroid (new one) explodes, stop checking

            else:
                stack.append(asteroid)  # If no collision, add it to the stack

        return stack        

#asteroids = [5, 10, -5, -10, 15]    

my_soln = Solution() #create an instance of solution
print(my_soln.asteroidCollision([5,10,-5]))
print(my_soln.asteroidCollision([8,-8]))