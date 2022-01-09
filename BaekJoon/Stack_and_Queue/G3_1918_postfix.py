## 1918. 후위 표기법 (01.09) G3
fix = input()
stack = []
answer = ""
for f in fix:
    if f.isalpha():
        answer += f
    else:
        if f == "(":
            stack.append(f)
        elif f == "*" or f == "/":
            while stack and (stack[-1] == "*" or stack[-1] == "/"):
                answer += stack.pop()
            stack.append(f)
        elif f == "+" or f == "-":
            while stack and stack[-1] != "(":
                answer += stack.pop()
            stack.append(f)
        elif f == ")":
            while stack and stack[-1] != "(":
                answer += stack.pop()
            stack.pop()

while stack:
    answer += stack.pop()
print(answer)