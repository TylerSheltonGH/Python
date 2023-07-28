# Arrange arithmetic problems vertically with optional answers.
def arithmetic_arranger(problems, show_answer = False):
    # Check if the number of problems is greater than 5.
    if len(problems) > 5:
        return "Error: Too many problems."
    
    # Initialize four empty lists to store the lines of each problem.
    line1, line2, line3, line4 = [], [], [], []

    # Loop through each problem in the list of problems.
    for problem in problems:
        
        # Split the problem into its components: operand1, operator, and operand2.
        operand1, operator, operand2 = problem.split()
       
        # Check if the operator is valid (+ or -).
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        # Check if both operands are composed of digits.
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."

        # Check if either operand has more than four digits.
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # Calculate the maximum length needed for proper alignment of the lines.
        max_length = max(len(operand1), len(operand2)) + 2
        
        # Right-justify the first operand and append it to line1.
        line1.append(operand1.rjust(max_length))

        # Right-justify the operator and the second operand, then append them to line2.
        line2.append(operator + operand2.rjust(max_length - 1))

        # Append a line of dashes with the same length as the maximum length.
        line3.append('-' * max_length)

        # If show_answer is True, evaluate the problem and right-justify the result, then append it to line4.
        if show_answer:
            result = str(eval(problem))
            line4.append(result.rjust(max_length))
    
    # Join each line of the problem using four spaces as the separator, and store them in arranged_lines.
    arranged_lines = ['    '.join(line) for line in [line1, line2, line3]]
    
    # If show_answer is True, join the line containing the results using four spaces as the separator, and add it to arranged_lines.
    if show_answer:
        arranged_lines.append('    '.join(line4))
    
    # Join all the lines with newlines to create the final arranged_problems string.
    arranged_problems = '\n'.join(arranged_lines)

    # Return the final arranged_problems string.
    return arranged_problems

# Test case
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True))