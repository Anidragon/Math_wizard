import re
from sympy import symbols, integrate, sin, cos, tan, log, exp

def symbolic_integration(expression, variables):
    vars = [symbols(var) for var in variables]
    int_expr = integrate(expression, *vars)
    return int_expr

def parse_expression(expression):
    expression = expression.replace('^', '**')

    # Replace math functions with valid Python function calls
    expression = re.sub(r'sin\((.*?)\)', r'sin(\1)', expression, flags=re.IGNORECASE)
    expression = re.sub(r'cos\((.*?)\)', r'cos(\1)', expression, flags=re.IGNORECASE)
    expression = re.sub(r'tan\((.*?)\)', r'tan(\1)', expression, flags=re.IGNORECASE)
    expression = re.sub(r'log\((.*?)\)', r'log(\1)', expression, flags=re.IGNORECASE)
    expression = re.sub(r'exp\((.*?)\)', r'exp(\1)', expression, flags=re.IGNORECASE)

    return expression


expression = input("Enter a mathematical expression: ")
variables = input("Enter the variables to integrate with respect to (comma-separated): ").split(',')

expression = parse_expression(expression)
integrated_expr = symbolic_integration(expression, variables)

print("Integrated expression:", integrated_expr)
