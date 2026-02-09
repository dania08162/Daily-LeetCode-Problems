# Daily-LeetCode-Problems
A daily record of LeetCode problems solved in Python!

# Day 1 - Two Sum Problem (Python)
  - **Intuition**
    The problem is basically checking which indexes can add up to the target. My first thought was to use a for-loop to go through each index and
    check which one can add to the target; if the number does not work, move on to the next one.

  - **Approach**
     For example, if the target was 5 and the zero index was 3, the code would keep 3 in mind and move on to check the
    next index, in this case maybe it is 1. 3 + 1 does not add up to 5, so it would skip it and move on to the next index which could be 2. 3+2 add up to 5, so the code would print what indexes 3 and 2 are!

  - **Complexity**
    - Time complexity:
      0(n), because we only go through the list once. 

    - Space complexity:
     0(n), since everything gets stored into the dictionary once.
      
# Day 2 - Palindrome Number Problem (Python)
  - **Intuition**
      For this problem, I have to check if a number flipped around is the same as the orignal number.
      
  - **Approach**
      First, I converted the number to a string so that it would be easy to flip. Then, I reversed the number and used an if statement to check if it is the same as the orginal number. Numbers that are negative would automatically not work because the negative sign would not be in the correct place.
      
- **Time Complexity**
  O(n), because reversing string only takes that.
  
# Day 3 - Lousey Christmas Presents (Python, not LeetCode)
  - **Intution**
    The problem is asking to find the longest sequence of a scarf that starts with a specific color and ends with a specific color.
    
  - **Approach**
    For this problem, I looped through the scarf and looked for positions where the starting color appears, and did the same for the ending color. Then I used a formula last[b] - first[a] + 1 each time and kept track of the maximum.

  - **Time Complexity**
    O(n), because the number of times we look at the scarf changes a lot.
