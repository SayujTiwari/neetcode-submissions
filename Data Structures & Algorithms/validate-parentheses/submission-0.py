class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if len(stack) == 0:
                stack.append(c)
            elif c == "]":
                if len(stack) == 0:
                    return False

                item = stack.pop(-1)
                if item == "[":
                    continue
                else:
                    return False
            elif c == "}":
                if len(stack) == 0:
                    return False
                item = stack.pop(-1)                
                if item == "{":
                    continue
                else:
                    return False
            elif c ==")":
                if len(stack) == 0:
                    return False
                item = stack.pop(-1)
                if item == "(":
                    continue
                else:
                    return False
            else:
                stack.append(c)
        return len(stack) == 0
                
                
