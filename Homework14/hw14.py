

#If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...

# Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
#
def friend(x):
    lst = [i for i in x if len(i) == 4]
    return lst


# At the end of the first year there will be:
# 1000 + 1000 * 0.02 + 50 => 1070 inhabitants
#
# At the end of the 2nd year there will be:
# 1070 + 1070 * 0.02 + 50 => 1141 inhabitants (** number of inhabitants is an integer **)
#
# At the end of the 3rd year there will be:
# 1141 + 1141 * 0.02 + 50 => 1213
#
# It will need 3 entire years.


#More generally given parameters:

# p0, percent, aug (inhabitants coming or leaving each year), p (population to equal or surpass)
#
# the function nb_year should return n number of entire years needed to get a population greater or equal to p.
#
# aug is an integer, percent a positive or null floating number, p0 and p are positive integers (> 0)
#
# Examples:
# nb_year(1500, 5, 100, 5000) -> 15
# nb_year(1500000, 2.5, 10000, 2000000) -> 10

def nb_year(population_start, percent, aug, population_target):
    population_progress = population_start
    counter = 0
    while population_progress < population_target:
        population_progress = population_progress + int((population_progress*percent/100)) + aug
        counter += 1
    print(counter)
    return counter

#Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).
class Solution(object):
    def removeElement(self, nums, val):
        while val in nums:
            nums.remove(val)