'''

Evaluate Reverse Polish Notation
Medium
Topics
Company Tags
Hints
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
Example 1:

Input: tokens = ["1","2","/","6","*","4","-"]

res = 3 /6  3 
stack = [3,3] * 
res = 9
stack = [9,4]
res = stac

Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5

'''


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0
        for x in tokens:
                if x == "+":
                    res = stack.pop() + stack.pop()
                    stack.append(res)
                elif x == "*":
                    res = stack.pop() * stack.pop()
                    stack.append(res) 
                elif x == "-": 
                    first = stack.pop()
                    second = stack.pop()
                    res = second - first
                    stack.append(res) 
                elif x == "/":
                    a , b = stack.pop(), stack.pop()
                    res = (int(float(b) / a))
                    stack.append(res) 
                else:
                    x = int(x)
                    stack.append(x)

        return stack[0]
         
         
        
        
