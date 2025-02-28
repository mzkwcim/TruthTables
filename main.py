from sympy import *
from sympy.logic.boolalg import to_dnf, Or, And, Not, Xor, simplify_logic

x, y = symbols('x y')

or_expression = x | y
print(f"OR: {or_expression}")

not_expression = ~x  
print(f"NOT: {not_expression}")

and_expression = x & y
print(f"AND: {and_expression}")

xor_expression = Xor(x, y)
print(f"XOR: {xor_expression}")

nor_expression = Not(x | y) 
print(f"NOR: {nor_expression}")

x1, x2 = symbols('x1 x2')
complex_expression = Xor(1, (x1 & x2))
print(f"Złożone wyrażenie: 1 XOR (x1 AND x2) = {complex_expression}")

simplified_complex_expression = simplify_logic(complex_expression)
print(f"Uproszczone złożone wyrażenie: {simplified_complex_expression}")

pks_complex_expression = to_dnf(complex_expression)
print(f"PKS dla złożonego wyrażenia: {pks_complex_expression}")

def truth_table(expression, variables):
    print("\nTabela Prawdy:")
    print(f"{variables} | Wynik")
    print("-------" + "-|-------")
    for i in range(2**len(variables)):
        values = {}
        for j, var in enumerate(variables):
            values[var] = bool((i >> j) & 1)
        result = expression.subs(values)
        print(f"{[values[var] for var in variables]} | {result}")

truth_table(complex_expression, [x1, x2])