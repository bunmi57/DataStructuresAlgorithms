'''
Steps
Step 1: Understand the Problem
Step 2: Identify Inputs and Outputs
Step 3: Break it into Steps
    Create a dictionary to count occurrences of each character.
    Loop through the string again, and return the first character that appears only once.
    If no unique character is found, return None.
Step 4: Identify Edge Cases
    "aabb" → No unique characters, should return None.
    "abcdef" → The first character is always unique, should return 'a'.
    "aabbccddeef" → Only the last character 'f' is unique.

Logic in plain English
Create an empty dictionary (count_dict).
Loop through the string and count occurrences of each character.
Loop again through the original string, and return the first character that appears only once.
If no unique character is found, return None.
'''
arr1 = "leetcode"
arr2 = "loveleetcode"
arr3 = "aabb" 
arr4 = "abcdef"
arr5 = "aabbccddeef"

def firstUniqueCharacter(arr):
    #Empty dictionary to store count of charcters 
    count_dict = {}

    #loop through the string and count occurrences of each character
    for letter in arr:
        #Block of code can be updated to count_dict[letter] = count_dict.get(letter,0) + 1
        if letter not in count_dict:
            count_dict[letter] = 1
        else:
            count_dict[letter] +=  1
    
    for letter in arr:
        if count_dict[letter] == 1:
            return letter
    
    return None
    

print(firstUniqueCharacter(arr2))


