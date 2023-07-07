import re
from sympy import symbols, diff, sin, cos, tan, log, exp

def symbolic_differentiation(expression):
    x = symbols('x')
    diff_expr = diff(expression, x)
    return diff_expr

def parse_expression(expression):
    expression = expression.replace('^', '**')
    expression = re.sub(r'sin\((.*?)\)', r'sin(\1)', expression, flags=re.IGNORECASE)
    expression = re.sub(r'cos\((.*?)\)', r'cos(\1)', expression, flags=re.IGNORECASE)
    expression = re.sub(r'tan\((.*?)\)', r'tan(\1)', expression, flags=re.IGNORECASE)
    expression = re.sub(r'log\((.*?)\)', r'log(\1)', expression, flags=re.IGNORECASE)
    expression = re.sub(r'exp\((.*?)\)', r'exp(\1)', expression, flags=re.IGNORECASE)
    return expression

expression = input("Enter a mathematical expression: ")
variable = input("Enter the variable to differentiate with respect to: ")

expression = parse_expression(expression)
differentiated_expr = symbolic_differentiation(expression)
result = diff(differentiated_expr, symbols(variable))

print("Differentiated expression:", result)
