"""
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
"""

#Solution
class Solution:
    
    def solution(self,s: str) -> str:
        s2 = ""
        for char in s :
            if char == '#':
                if s2:
                    s2 = s2[:-1]
            else:
                s2 += char
                
        return s2
    
    def backspaceCompare(self, S: str, T: str) -> bool:
        
        
        return self.solution(S) == self.solution(T)
