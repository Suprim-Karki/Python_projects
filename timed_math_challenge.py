''' Timed Math Chalenge'''

import random

operators=['+','-','*']
min_operand=3
max_operand=12

def generate_problem():
    left=random.randint(min_operand,max_operand)
    right=random.randint(min_operand,max_operand)
    operator=random.choice(operators)

    expression = f"{left} {operator} {right}"
    return expression

print(generate_problem())