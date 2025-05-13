'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
'''

def isSubsequence(s,t):
    #if len of s > len of t return false 
    if len(s) > len(t):
        return False
    #for an empty string
    if len(s) == 0:
        return True
    #use 2 pointer technique - 1 pointer to loop s and another for t 
    ps = 0
    pt = 0

    #check if letter in t is same as letter in s, if it is add 1 to the counter, if the counter is equal to the length
    #of s, then means all the letters in s have been found and this is in order so return True
    for letter in t:
        if letter == s[pt]:
            pt += 1
        if pt == len(s):
            return True
    
    return False

print(isSubsequence(s = "axc", t = "ahbgxc"))