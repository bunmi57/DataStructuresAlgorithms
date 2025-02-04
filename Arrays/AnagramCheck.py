'''
Given two strings, check to see if they are anagrams
"clint eastwood" is an anagram of "old west station
"public relations" is an anagram of "crap built on lies"
'''
# s1 = "clint eastwood"
# s2 = "old west action"
s1 = "public relations"
s2 = "crap built on lies"

def AnagramCheck(s1,s2):
    #remove spaces in string and convert to a list
    s1 = list("".join(s1.split()))
    s2 = list("".join(s2.split()))
  
    #check the length of the 2 strings
    s1_len = len(s1)
    s2_len = len(s2)

    #if s1 length is not equal to s2 length,can't be an anagram, return False
    if s1_len != s2_len:
        return False
    else:#remove every character in s1 that occurs in s2
        for char in s1:
            if char in s2:
                s2.remove(char)
        return len(s2) == 0 #if length is 0, the 2 strings are anagrams
            
print(AnagramCheck(s1,s2))
print(sorted(s1))

#Another Solution
def anagram(s1,s2):

    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    #Edge case check
    if len(s1) != len(s2):
        return False
    
    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
    
    for k in count:
        if count[k] != 0:
            return False
    return True
    

print(anagram(s1,s2))