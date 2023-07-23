def is_balanced(input):
    stack = []
    for char in input:
        if char in "([{":
            stack.append(char)
        elif char in "}])":
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(' and char != ')' or \
            current_char == '[' and char != ']' or \
            current_char == '{' and char != '}':
                return False
    return not stack

while True:
    user_input = input("Enter a string of paratheses: ")
    if is_balanced(user_input):
        print("The string of parantheses is balanced.")
    else:
        print("The string of parantheses is not balanced.")
