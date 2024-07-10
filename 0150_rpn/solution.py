import operator
    
operations = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}
    
def eval_rpn(tokens):
    stack = []
    lhand_operand = None
    rhand_operand = None
    operators_list = {"+", "-", "*", "/"}
    for c in tokens:
        if c not in operators_list :
            if lhand_operand != None:
                stack.append(lhand_operand)
            lhand_operand = rhand_operand
            rhand_operand = int(c)
        else:
            operation = operations[c]
            rhand_operand = int(operation(lhand_operand, rhand_operand))
            lhand_operand = None if len(stack) == 0 else stack.pop()
                
    return rhand_operand

class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        return eval_rpn(tokens)


sol = Solution()
tokens = ["4","13","5","/","+"]
result = sol.evalRPN(tokens)
print(result)
