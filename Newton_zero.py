from sympy import symbols, cos
from sympy import simplify

x = symbols('x')
f = x ** 2 + cos(x) ** 2 - 4 * x

f1 = f.diff(x)
f2 = f1.diff(x)

x0 = 10
# step = 0.001
# x1 = 3
step = True
iterations = 0
while step:
    x1 = x0 - round(f.subs(x, x0), 7) / round(f1.subs(x, x0), 7)
    error = abs(x0 - x1)
    if error < 0.0001:
        step = False
        print('Found solution after', iterations, 'iterations.')

    elif (round(f1.subs(x, x0), 7)) == 0:
        print('Zero derivative. No solution found.')

    else:
        x0 = x1
    iterations += 1


print(x1)
