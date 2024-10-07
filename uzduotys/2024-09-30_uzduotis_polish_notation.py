
def evaluate_rpn(expression):
    stack = []
    operators = {'+', '-', '*', '/'}

    for token in expression:
        if token not in operators:
            stack.append(int(token))
        else:
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  # Ensure integer division

    return stack[0]

# Example usage:
expression = ["2", "1", "+", "3", "*"]
print(evaluate_rpn(expression))  # Output: 9


def evaluate_polish(expression):
    def helper(index):
        token = expression[index]
        if token == '(':
            operator = expression[index + 1]
            left_val, next_index = helper(index + 2)
            right_val, next_index = helper(next_index)
            if expression[next_index] != ')':
                raise ValueError("Mismatched parentheses")
            next_index += 1
            if operator == '+':
                return left_val + right_val, next_index
            elif operator == '-':
                return left_val - right_val, next_index
            elif operator == '*':
                return left_val * right_val, next_index
            elif operator == '/':
                return int(left_val / right_val), next_index
        else:
            return int(token), index + 1

    result, _ = helper(0)
    return result

# Example usage:
# expression = ["(", "+", "2", "(", "*", "3", "4", ")", ")"]
expression = '(+2(*34))'
print(evaluate_polish(expression))  # Output: 14
