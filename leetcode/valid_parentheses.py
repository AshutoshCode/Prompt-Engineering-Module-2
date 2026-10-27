"""LeetCode 20 - Valid Parentheses (Easy).

Given a string of ()[]{} decide whether brackets are closed in the correct order.
Stack approach: O(n) time, O(n) space.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {")": "(", "]": "[", "}": "{"}
        stack = []
        for ch in s:
            if ch in pairs:
                if not stack or stack.pop() != pairs[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack


if __name__ == "__main__":
    s = Solution()
    assert s.isValid("()") is True
    assert s.isValid("()[]{}") is True
    assert s.isValid("(]") is False
    assert s.isValid("([)]") is False
    assert s.isValid("{[]}") is True
    assert s.isValid("(") is False      # unclosed
    assert s.isValid("]") is False      # closer with empty stack
    print("valid_parentheses: all tests passed")
