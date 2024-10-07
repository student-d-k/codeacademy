
# leetcode 2491

from typing import List

import re
import time

class Solution:

    def dividePlayers(self, skill: List[int]) -> int:


        def case1():

            if min(skill) < 1:
                return -1
            
            t_len = len(skill)
            n_teams = t_len / 2
            t_sum = sum(skill)

            if t_len % 2 != 0:
                return -1

            if t_len == 2:
                return skill[0] * skill[1]

            if t_sum % 2 != 0:
                return -1

            total_skill = t_sum / n_teams

            r = []

            for i, e in enumerate(skill):

                for j, e2 in enumerate(skill):

                    if i == j:
                        break

                    if e + e2 == total_skill:
                        r.append((e, e2))
                        skill[i] = -1
                        skill[j] = -1
                        if len(r) == n_teams:
                            break

            if len(r) != n_teams:
                return -1
            else:
                return(sum([t[0] * t[1] for t in r]))
        

        count_try = 1
        r = 0
        for i in range(0, count_try):
            r = case1()

        return r


# tests

skill = [3,2,5,1,3,4]
# skill = [3,4]
# skill = [1,1,2,3]

start_time = time.time()
print(Solution().dividePlayers(skill))
print(f'{round(1000 * (time.time() - start_time))} ms')
