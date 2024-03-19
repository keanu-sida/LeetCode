# First Attempt:

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        last_jump, gap, current = int(0), int(0), int(0)                            # initializing variables for the previous jump length, next gap length, and current stone
        if stones[1] - stones[0] > 1:                                               # making sure first stone is only one unit away (otherwise fail)
            return False
        for stone in stones:                                                        # linear loop to see if a simple jump sequence exists... we will need to d oa DFS search instead.
            gap = stones[stone+1] - stones[stone]
            if gap == last_jump | gap == last_jump + 1 | gap == last_jump - 1:
                last_jump = stones[stone+1] - stones[stone]
                current = stone + 1
            else:
                return False

# Second Attempt, with some rough guidance. This solution passed 51/52 test cases. Exception: [0,1,2,5,6,9,10,12,13,14,17,19,20,21,26,27,28,29,30]
from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[1] != 1:                                      # ensures that first jump is possible, since it must be 1 and stones[0] == 0
            return False                                                            
        
        jump_map = {stone: set() for stone in stones}           # initializes a jump map containing an empty set for each stone in the list. Each set will contain all the
                                                                # possible jump distances to be made at that specific stone. 
        jump_map[stones[0]].add(1)                              # add 1 as a possible distance to the first stone, since we tested above to ensure this is possible

        for stone in stones:
            for jump in jump_map[stone]:
                for step in [-1, 0, 1]:
                    next_jump = jump + step
                    if next_jump <= 0:
                        continue

                    next_stone = stone + next_jump
                    if next_stone == stones[-1]:
                        return True
                    
                    if next_stone in jump_map:
                        jump_map[next_stone].add(next_jump)

        return False
    
    # Third Attempt, chatGPT assisted, using memoization. Successful with 85.57%ile runtime and 57%ile memory

    class Solution:
        def canCross(self, stones):
            if not stones:
                return False

            target = stones[-1]
            stones_set = set(stones)
            memo = {} # To remember if a stone with a given jump distance can lead to the end

            def dfs(position, jump):
                if position == target:
                    return True
                if (position, jump) in memo:
                    return memo[(position, jump)]

                # Possible next jumps: jump-1, jump, jump+1
                for next_jump in {jump - 1, jump, jump + 1}:
                    if next_jump > 0 and position + next_jump in stones_set:
                        if dfs(position + next_jump, next_jump):
                            return True

                memo[(position, jump)] = False
                return False

            return dfs(0, 0)