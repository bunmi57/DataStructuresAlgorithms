'''
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.


'''
candies = [2,3,5,1,3]
extraCandies = 3
def greatestCandies(candies,extraCandies):
    #find the max number of candies 
    max_candies = max(candies)

    #initialize result array 
    result = []

    #add extra candies to candies of each child
    for candy in candies:
        new_candy_number = candy + extraCandies
        #compare the new number of candies to the max
        comparison = new_candy_number >= max_candies
        result.append(comparison)
    return result 

print(greatestCandies(candies,extraCandies))