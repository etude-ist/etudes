"""
Balanced Delimiters

I heard today's exercise as an interview question - you have five minutes
to solve this task, while I watch - but it could equally be a homework problem:

Write a function to return true/false after looking at a string.
Examples of strings that pass:

{}, [], (), a(b)c, abc[d], a(b)c{d[e]}

Examples of strings that don't pass:

{], (], a(b]c, abc[d}, a(b)c{d[e}]

http://programmingpraxis.com/2014/06/10/balanced-delimiters-2/
"""


def balanced(s):
    symbols = ['{', '}', '(', ')', '[', ']']
    rewrite = {'}': '{', ')': '(', ']': '['}
    stack = []
    for l in s:
        if len(stack) > 0 and rewrite.get(l) == stack[-1]:
            stack.pop()
        elif l in symbols:
            stack.append(l)
    return len(stack) == 0


def tests():
    balanced_input = ['{}', '[]', '()', 'a(b)c', 'abc[d]', 'a(b)c{d[e]}']
    assert all(balanced(s) for s in balanced_input)
    inbalanced_input = ['{]', '(]', 'a(b]c', 'abc[d}', 'a(b)c{d[e}]']
    assert all(not balanced(s) for s in inbalanced_input)
    print('Tests passed!')
