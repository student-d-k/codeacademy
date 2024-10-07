
# leetcode 1684

from typing import List

import re
import time

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        def case1():
            return sum([len(re.sub('['+allowed+']', '', w)) == 0 for w in words])

        def case2():
            # Convert the allowed string into a set for faster membership testing
            a = set(allowed)
            
            # Initialize the count of consistent words
            c = 0
            
            # Iterate over each word in the list of words
            for word in words:
                # Check each letter in the current word
                for letter in word:
                    # If the letter is not in the set of allowed characters, break out of the loop
                    if letter not in a:
                        break
                # If the loop completes without breaking, all letters in the word are allowed
                else:
                    # Increment the count of consistent words
                    c += 1
            
            # Return the total count of consistent words
            return c

        count_try = 100000
        r = 0
        for i in range(0, count_try):
            r = case2()

        return r

# tests

allowed = "ab"
words = ["ad", "bd", "aaab", "baa", "badab"]

allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]

allowed = "cad"
words = ["cc","acd","b","ba","bac","bad","ac","d"]

start_time = time.time()
print(Solution().countConsistentStrings(allowed, words))
print(round(1000 * (time.time() - start_time)))
