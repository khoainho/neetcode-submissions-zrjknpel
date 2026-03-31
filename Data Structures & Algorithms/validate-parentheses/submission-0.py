class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {")":"(", "]":"[", "}":"{"}

        for i in s:
            if i in map:
                if stack and stack[-1] == map[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
                print(stack)
        return True if not stack else False