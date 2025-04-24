''' Timed Math Chalenge'''

import random
import time

OPERATORS=['+','-','*']
MIN_OPERAND=3
MAX_OPERAND=12
total_problems=10

def generate_problem():
    left=random.randint(MIN_OPERAND,MAX_OPERAND)
    right=random.randint(MIN_OPERAND,MAX_OPERAND)
    operator=random.choice(OPERATORS)

    expression = f"{left} {operator} {right}"
    ans=eval(expression)
    return expression, ans


wrong=0
input("Press enter to start: ")
print("----------------------")

start_time=time.time()

for i in range(total_problems):
    expression,ans=generate_problem()
    while True:
        guess = input(f"Problem {i+1}\n{expression}: ")
        if guess==str(ans):
            break
        wrong+=1

end_time=time.time()
total_time=end_time-start_time
print("-----------------------")
print(f"Nice Work! You finished in {total_time:.2f} seconds")