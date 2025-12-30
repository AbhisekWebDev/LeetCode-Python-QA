class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        result = []

        def backtrack(curr, open, close):
            # When valid combination formed
            if len(curr) == 2 * n:
                result.append(curr)
                return
            
            # Try adding (
            if open < n:
                backtrack(curr + "(", open + 1, close)
            
            # Try adding )
            if close < open:
                backtrack(curr + ")", open, close + 1)

        backtrack("", 0, 0)
        return result


# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

# Example 1:

# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:

# Input: n = 1
# Output: ["()"]
 

# Constraints:

# 1 <= n <= 8