import operator

OPERATORS = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def evaluate(expression):
    tokens = expression.split()
    stack = []
    for token in tokens:
        if token in OPERATORS:
            if len(stack) < 2:
                raise ValueError("Invalid expression. Not enough operands.")
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = OPERATORS[token](operand1, operand2)
            stack.append(result)
        else:
            try:
                stack.append(float(token))
            except ValueError:
                raise ValueError("Invalid token '{}'".format(token))
    if len(stack) != 1:
        raise ValueError("Invalid expression. Too many operands.")
    return stack[0]

def main():
    print("Welcome to the FLEXICODE.")
    print("Supported operations: +, -, *, /")
    print("Enter an expression (or 'exit' to quit): ")
    while True:
        expression = input(">> ")
        if expression.lower() == 'exit':
            break
        try:
            result = evaluate(expression)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
