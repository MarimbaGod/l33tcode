# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

# we can use sorted(string) to sort both strings

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sorted_s = sorted(s)
        sorted_t = sorted(t)
        return sorted_s == sorted_t

    # OR use a hash table:
    def checkAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int) # initialize the count hashmap

        # Count char in str s
        for char in s:
            count[char] += 1

        #decrement count for char in str t
        for char in t:
            count[char] -= 1

        #If anagram, they should cancel eachother into 0

        for value in count.values():
            if value != 0:
                return False
            else:
                return True
        return True
