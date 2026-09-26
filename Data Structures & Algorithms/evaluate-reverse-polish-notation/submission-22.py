class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []
        for i in tokens:
            if i == "+":
                result = stack.pop() + stack.pop()
                stack.append(result)


            elif i == "-":
                a = stack.pop()
                b = stack.pop()
                result = b - a
                stack.append(result)

            elif i == "*":
                result = stack.pop() * stack.pop()
                stack.append(result)


            elif i == "/":
                a = stack.pop()
                b = stack.pop()
                result = int(b / a)
                stack.append(result)

            else:
                stack.append(int(i))
        return stack[0]

