"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string.
An empty string is also valid.
Example 1:
Input: "()"
Output: True
Example 2:
Input: "(*)"
Output: True
Example 3:
Input: "(*))"
Output: True

"""

class Solution:
    def checkValidString(self, s: str) -> bool:
        
        stack = []
        prev = 0
        star = []
        l = len(s)
    
                
        for i in range(l):
                
            if s[i] == '(' :
                stack.append(i)
                
            elif s[i] == ')' :
                
                if stack:
                    indx = stack.pop(-1) 
                    
                else:
                    if star:
                        star.pop(-1)
                                               
                    else:
                        
                        return False
                    
            else :
                star.append(i)
                
        if stack :
            l = len(stack)
            if star and len(star) >= l:
                for indx in range(l-1, -1, -1):
                    if stack[indx] < star[-1]:
                        star.pop(-1)
                    else:
                        
                        return False
            else:
                
                return False
        return True
