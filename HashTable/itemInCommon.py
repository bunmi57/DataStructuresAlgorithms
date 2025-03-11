'''
Given 2 lists as input 
return True if at least 1 common element between lists

'''
def item_in_common(list1,list2):
    #create a dictionary
    dict_item = {}
    #for each element in list 1, add in dictionary
    for element in list1:
        dict_item[element] = True
    for element in list2:
        if element in dict_item:
            return True
    return False
list1 = [1,3,5]
list2 = [2,4,5]
print(item_in_common(list1,list2))

