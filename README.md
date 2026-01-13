# Daily-LeetCode-Problems
A daily record of LeetCode problems solved in Python!

**Day 1** - Two Sum Problem (Python)
  - # Intuition
        <!-- Describe your first thoughts on how to solve this problem. --> The problem is basically checking which indexes can add up to the target. My first thought was to use a for-loop           to go through each index and check which one can add to the target; if the number does not work, move on to the next one.

  - # Approach
        For example, if the target was 5 and the zero index was 3, the code would keep 3 in mind and move on to check the next index, in this case maybe it is 1. 3 + 1 does not add up to 5, so it would skip it and move on to the next index which could be 2. 3+2 add up to 5, so the code would print what indexes 3 and 2 are!

  - # Complexity
      - Time complexity:
       0(n), because we only go through the list once. 

      - Space complexity:
       0(n), since everything gets stored into the dictionary once. 
