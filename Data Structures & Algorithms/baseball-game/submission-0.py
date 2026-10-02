class Solution:
    def calPoints(self, operations: List[str]) -> int:
        #if int number append to the stack
        #if + append the sum of the two previous 
        #
        # [1, 2, 5, 10]
        stack = []
        

        for op in operations:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            elif op == "D":
                stack.append(2 * stack[-1])
            elif op == "C":
                stack.pop()
            else:
                stack.append(int(op))
        
        return sum(stack)

        