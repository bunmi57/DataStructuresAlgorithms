
def mergeStrings(word1, word2):
    #create output string 
    output = ""

    #create 2 pointers, i and j
    i = 0
    j = 0

    #iterate through string 
    while i < len(word1) and j < len(word2): #while len of word 1 and word 2 are same
        output += word1[i]
        output += word2[j]
        i += 1
        j += 1
    if len(word1) > i:
        output += word1[i:]
    if len(word2) > j:
        output += word2[j:]

    return output


#optimized code
def mergeStrings_optimized(word1, word2):
    #create output string 
    output =  []

    #create 2 pointers, i and j
    i = 0
    j = 0

    #iterate through string 
    while i < len(word1) and j < len(word2): #while len of word 1 and word 2 are same
        output.append(word1[i])
        output.append(word2[j])
        i += 1
        j += 1

    
    output += word1[i:]
    output += word2[j:]

  
    return  "".join(output) #joins all elements of the list into a single string

word1 = 'abc'
word2 = 'pqr'
word3 = 'ab'
word4 = 'pqrs'
word5 = 'abcd'
word6 = 'pq'

# print('apbqcr: ',mergeStrings(word1,word2))
print('apbqrs', mergeStrings(word3, word4))
print('apbqcd', mergeStrings_optimized(word5, word6))