class Solution:
    def isValid(self, s: str) -> bool:
        # use a stack: pop, push, peek
        # let the computer know what's valid
        # using a dictionary
        # pop them if they match
        # left with an empty stack

        stack = []
        valid = { ")" : "(", "]" : "[", "}" : "{" }

        for char in s:
            if char in valid:
                if stack and stack[-1] == valid[char]:
                    stack.pop() 
                else:
                    return False
            else:
                stack.append(char)
        #return true if stack is empty
        return True if not stack else False

        
        
        
        
