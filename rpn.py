"""Implement an RPN calculator that takes an expression like 19 2.14 + 4.5 2 4.3 / - * which is usually expressed as (19 + 2.14) * (4.5 - 2 / 4.3) and responds with 85.2974."""

OPS = set(['+', '-', '*', '/'])

def rpc_calc(rpc_exp, ops=OPS):
    stack = []
    for exp in rpc_exp:
        if exp in ops:
            a = stack.pop()
            b = stack.pop()
            stack.append("({} {} {})".format(b, exp, a))
        else:
            stack.append(exp)
    return stack.pop()
