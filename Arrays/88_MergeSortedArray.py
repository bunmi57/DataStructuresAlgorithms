class Solution(object):
    def merge(self, nums1, m, nums2, n):
        #Edge case
        if m == 0:
           nums1[:n] = nums2
       

        #use 2 pointer 
        #initialize pointers 
        i = m-1
        j = n -1
        p = m + n - 1

        #compare value at i and j
        while i >=0 and j>=0:
            #i > j
            if nums1[i] > nums2[j]:
                nums1[p] = nums1[i] #move value at i to index p
                i -= 1
                p -= 1
            elif nums1[i] == nums2[j]:
                nums1[p] = nums1[i] #move value at i to index p
                nums1[p-1] = nums2[j] #move value at j to index p-1
                j -= 1 #move index j by -1
                i -= 1#move index i by -1
                p -= 2
            else:
                nums1[p] = nums2[j] #move value at j to index p
                j -= 1 #move index j by -1
                p -= 1

        if j >= 0:
            nums1[0:j+1] = nums2[0:j+1]

        return nums1

# nums1 = [4,6,7,0,0,0]
# nums2 = [2,3,4]
nums1 = [2,0]
nums2 = [1]
m = 1
n = 1
sol = Solution()
print(sol.merge(nums1, m, nums2, n))