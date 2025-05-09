'''
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
Example 1:
Input: s = "IceCreAm"
Output: "AceCreIm"
Explanation:
The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".
'''
def reverseVowels(s):
    #define vowels in lower and upper cases
    vowels = ['a','e','i','o','u','A','E','I','O','U']

    #convert string to list
    str_to_list = list(s)

    #initialize a vowel list and position list
    vowel_list = []
    position_list = []

    #loop through the string and check if it is a vowel
    for i in range(len(s)):
        #check if it is a vowel 
        if s[i] in vowels:
            vowel_list.append(s[i]) #and append to vowel list 
            position_list.append(i) # note the position of the vowel 

    #indialize an index that accesses the vowel list in revered order 
    index = -1
    #for each position in s where there is a vowel, add the reveresed vowel 
    for position in position_list:
        str_to_list[position] = vowel_list[index]
        index -= 1 

    return ''.join(str_to_list)

print(reverseVowels(s = "IceCreAm")) # "AceCreIm"
print(reverseVowels(s = "leetcode")) # "leotcede"


