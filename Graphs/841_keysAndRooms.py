'''
There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. 
Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.

When you visit a room, you may find a set of distinct keys in it.
Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.

Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i,
return true if you can visit all the rooms, or false otherwise.

Example 1:

Input: rooms = [[1],[2],[3],[]]
Output: true
Explanation: 
We visit room 0 and pick up key 1.
We then visit room 1 and pick up key 2.
We then visit room 2 and pick up key 3.
We then visit room 3.
Since we were able to visit every room, we return true.
Example 2:

Input: rooms = [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.

'''


class Solution:
    def keysAndRooms(self,rooms):
        visited = set()

        def dfs(rooms,room,visited):
            if room not in visited:#Mark it as visited 
                visited.add(room)
                for key in rooms[room]: #visit all unvisited rooms, one by one,for each room, repeat the process,f stuck(no unvisited rooms), backtrack
                    dfs(rooms,key,visited)
            return visited
        
        visited_list = dfs(rooms,0,visited) #start with a room
        #check that all keys are in visited list
        for item in range(len(rooms)):
            if item not in visited_list:
                return False
        return True 

rooms = [[1],[2],[3],[]]
#create an instance of the class solution
soln1 = Solution()
print(soln1.keysAndRooms(rooms))