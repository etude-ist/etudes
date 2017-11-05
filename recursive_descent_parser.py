"""
Old grumpy programmer said: 25y ago, writing a recursive descent parser
was basic 1st/2nd year knowledge. Today an MSc commonly can't write one at all.

Task: Write toy recursive descent parser for a propositional calculus.
"""
import re


RE_WS_SKIP = re.compile(r"\S")


class Expr:
    def __init__(self, buf):
        self.buf = buf
        self.pos = 0

    def current(self):
        return self.buf[self.pos:]


def skip_whitespace(expr, skipper=RE_WS_SKIP):
    m = skipper.search(expr.current())
    expr.pos += m.start()


def match(expr, token):
    t = re.compile(token)
    m = t.match(expr.current())
    if m:
        expr.pos += len(m.group(0))
        return True
    else:
        return False


def is_constant(expr):
    initial = expr.pos
    skip_whitespace(expr)
    if match(expr, "T") or match(expr, "F"):
        return True
    expr.pos = initial
    return False


def is_proposition(expr):
    initial = expr.pos
    skip_whitespace(expr)
    if match(expr, "[a-z0-9]"):
        return True
    expr.pos = initial
    return False


def is_formula(expr):
    initial = expr.pos
    skip_whitespace(expr)
    if (is_constant(expr) or is_proposition(expr) or
            is_unary_formula(expr) or is_binary_formula(expr)):
        return True
    expr.pos = initial
    return False


def is_unary_formula(expr):
    initial = expr.pos
    skip_whitespace(expr)

    if not is_left_paren(expr):
        expr.pos = initial
        return False

    if not is_unary_operator(expr):
        expr.pos = initial
        return False

    if not is_formula(expr):
        expr.pos = initial
        return False

    if not is_right_paren(expr):
        expr.pos = initial
        return False

    return True


def is_binary_formula(expr):
    initial = expr.pos

    if not is_left_paren(expr):
        expr.pos = initial
        return False

    if not is_formula(expr):
        expr.pos = initial
        return False

    if not is_binary_operator(expr):
        expr.pos = initial
        return False

    if not is_formula(expr):
        expr.pos = initial
        return False

    if not is_right_paren(expr):
        expr.pos = initial
        return False

    return True


def is_unary_operator(expr):
    initial = expr.pos
    skip_whitespace(expr)

    if match(expr, r"\~"):
        return True

    expr.pos = initial
    return False


def is_binary_operator(expr):
    initial = expr.pos
    skip_whitespace(expr)

    if match(expr, r"\&") or match(expr, r"\+"):
        return True

    expr.pos = initial
    return False


def is_left_paren(expr):
    initial = expr.pos
    skip_whitespace(expr)

    if match(expr, r"\("):
        return True

    expr.pos = initial
    return False


def is_right_paren(expr):
    initial = expr.pos
    skip_whitespace(expr)

    if match(expr, r"\)"):
        return True

    expr.pos = initial
    return False


def parse(data):
    expr = Expr(data)
    skip_whitespace(expr)
    return is_formula(expr)


assert parse("T")
assert parse("   T")
assert parse("F")
assert parse("p")
assert parse("(~ p)")
assert parse("(p + q)")
assert parse("(p & q)")
assert parse("((p & q) + (q & p))")
assert parse("((p & (~q)) + (q & (~p)))")
print("Tests passed!")
