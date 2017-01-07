import sys
sys.stdin = open("input.txt")

T = int(raw_input())
match = {"]": "[", "}": "{"}
while T:
    T -= 1
    stack = list()
    error_flag = False
    push, pop, count = stack.append, stack.pop, 0
    data = raw_input().split()
    if data[0] == "{" and data[-1] == "}":
        del data[0], data[-1]
        for token in data:
            if token == "<":
                push(token)
            elif token == "(" and "<" not in stack:
                push(token)
            elif token == "{" and ("<" in stack or "(" in stack):
                push(token)
            elif token == "P" and count <= 100:
                count += 1
            elif token in ["}", ">", ")"]:
                x = pop()
                while x != match[token]:
                    x = pop()
            else:
                print "Compilation Errors"
                error_flag = True
        if stack and not error_flag:
            print "Compilation Errors"
        else:
            print "No Compilation Errors"
    else:
        print "Compilation Errors"
