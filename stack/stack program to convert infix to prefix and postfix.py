from queue import LifoQueue

class CustomLifo(LifoQueue):
    def top(self):
        num = self.get()
        self.put(num)
        return num


def infix_postfix(input_string):
    input_string = input_string.replace(" ", "")
    stack = CustomLifo(len(input_string))
    postfix = ""
    precedence = {'+':1, '-':1, '*':2, '/':2, '^':3}

    for char in input_string:

        if char == '(':
            stack.put(char)

        elif char == ')':
            while stack.top() != '(':
                postfix += stack.get()
            stack.get()

        elif char.isalnum():
            postfix += char

        else:
            if stack.empty() or stack.top() == '(' or precedence[char] > precedence[stack.top()]:
                stack.put(char)
            else:
                while (not stack.empty() and stack.top() != '(' and
                       precedence[char] <= precedence[stack.top()]):
                    postfix += stack.get()
                stack.put(char)

    while not stack.empty():
        postfix += stack.get()

    return postfix


def infix_prefix(input_string):
    input_string = input_string[::-1]
    input_string = input_string.replace('(', '#').replace(')', '(').replace('#', ')')
    prefix = infix_postfix(input_string)
    return prefix[::-1]


# -------- Driver code --------
expr = input("Enter infix expression: ")
print("Postfix Expression:", infix_postfix(expr))
print("Prefix Expression:", infix_prefix(expr))
