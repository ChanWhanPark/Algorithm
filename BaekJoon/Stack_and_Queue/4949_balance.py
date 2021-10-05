## 4949. 균형잡힌 세상 (10.05)
while True:
    string = input()
    stack = []
    if string == ".":
        break

    for s in string:
        if s == "(" or s == "[":
            stack.append(s)
        if s == ")":
            if len(stack) == 0:
                stack.append(s)
                break
            if stack[-1] == "(":
                stack.pop(-1)
            elif stack[-1] == "[":
                break
        if s == "]":
            if len(stack) == 0:
                stack.append(s)
                break
            if stack[-1] == "[":
                stack.pop(-1)
            elif stack[-1] == "(":
                break

    if len(stack) == 0:
        print("yes")
    else:
        print("no")