class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        bracket_map = {')': '(', '}': '{', ']': '['}
       
        stack = []
        
      
        for char in s:
            if char in bracket_map:
                # Pop the top element from the stack if not empty, else assign '#'
                top_element = stack.pop() if stack else '#'
                
                # If the mapping for this bracket doesn't match the stack's top, return False
                if bracket_map[char] != top_element:
                    return False
            else:
                # Push the opening bracket onto the stack
                stack.append(char)
        
        # In the end, if the stack is empty, then we have a valid set of parentheses
        return not stack
        pass







    



  

