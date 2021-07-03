class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for paren in s:
            if paren == "(":
                stack.append(")")
            elif paren == "{":
                stack.append("}")
            elif paren == "[":
                stack.append("]")
            elif stack:
                if stack.pop() != paren:
                    return False
            else:
                return False
        return True if not stack else False

