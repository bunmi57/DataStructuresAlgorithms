'''
Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.


Example 1:

Input: s = "abciiidef", k = 3
Output: 3
Explanation: The substring "iii" contains 3 vowel letters.
Example 2:

Input: s = "aeiou", k = 2
Output: 2
Explanation: Any substring of length 2 contains 2 vowels.
Example 3:

Input: s = "leetcode", k = 3
Output: 2
Explanation: "lee", "eet" and "ode" contain 2 vowels.

'''
def maxVowels(s,k):
    list_vowels = ['a','e','i','o','u']
    vowels = set(list_vowels) #vowels = {'a', 'e', 'i', 'o', 'u'}
    maximum_vowels = float('-inf')
    current_vowels = 0
    for letter in s[:k]:
        if letter in vowels:
            current_vowels += 1
    maximum_vowels = max(maximum_vowels,current_vowels)
    left = 0
    for right in range(k,len(s)):
        if s[right] in vowels:
            current_vowels += 1
        if s[left] in vowels:
            current_vowels -= 1
        maximum_vowels = max(maximum_vowels,current_vowels)
        left += 1
    return maximum_vowels

print(maxVowels("aaciiidef",3))
