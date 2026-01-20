def precedence(c):
    if c == '*' or c == '/' or c == '%' or c == '//':
        return 4
    elif c == '+' or c == '-':
        return 3
    elif c == '(':
        return 1
    else:
        return 0


def cal(n1, n2, op):
    if op == '*':
        return n1 * n2
    elif op == '/':
        return n1 / n2
    elif op == '%':
        return n1 % n2
    elif op == '//':
        return n1 // n2
    elif op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    else:
        return 0


expr = input("Enter the infix expression: ")
lexpr = expr.split(' ')

s1 = []        # operand stack
s2 = ['#']     # operator stack

for c in lexpr:
    if c.isdigit():
        s1.append(int(c))

    elif c == '(':
        s2.append(c)

    elif c == ')':
        op = s2.pop()
        while op != '(':
            x2 = s1.pop()
            x1 = s1.pop()
            s1.append(cal(x1, x2, op))
            op = s2.pop()

    else:
        top = s2[-1]
        if precedence(c) >= precedence(top):
            s2.append(c)
        else:
            op = s2.pop()
            while precedence(op) > precedence(c):
                x2 = s1.pop()
                x1 = s1.pop()
                s1.append(cal(x1, x2, op))
                op = s2.pop()
            s2.append(op)
            s2.append(c)

op = s2.pop()
while op != '#':
    x2 = s1.pop()
    x1 = s1.pop()
    s1.append(cal(x1, x2, op))
    op = s2.pop()

print("Result =", s1[0])
