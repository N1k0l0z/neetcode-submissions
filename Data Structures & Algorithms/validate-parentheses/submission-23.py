class Solution:
    def isValid(self, s: str) -> bool:
        # Odd-length strings can never be balanced
        if len(s) % 2 != 0:
            return False

        hashing = {"]": "[", "}": "{", ")": "("}
        stack = []

        for char in s:
            if char in hashing:  # If it's a closing bracket
                # Stack must not be empty AND top of stack must match
                if not stack or stack[-1] != hashing[char]:
                    return False
                stack.pop()  # O(1) pop operation
            else:
                stack.append(char)  # Opening bracket: push to stack

        # True only if all opening brackets were matched and popped
        return True if stack == [] else False