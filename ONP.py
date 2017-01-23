import string
stack = list()


def prec(char):
    if char == "^":
        return 5
    if char == "/" or char == "*":
        return 4
    if char == "+" or char == "-":
        return 3
    if char == "(" or char == ")":
        return 2
    else:
        return 0


def ONP(expr):
    post = list()
    while expr:
        char = expr[0]
        expr = expr[1:]
        if char in string.lowercase:
            post.append(char)
        elif char == "(":
            stack.append(char)
        elif char == ")":
            while stack and stack[-1] != "(":
                post.append((stack.pop()))
            stack.pop()
        else:
            while stack and prec(char) <= prec(stack[-1]):
                post.append((stack.pop()))
            stack.append(char)
    post += stack[::-1]
    return ''.join(post)

for _ in xrange(int(raw_input())):
    print ONP(raw_input())
