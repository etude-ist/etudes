"""
Drawing Diamonds
----------------

Given a small positive integer n, write a function that draws a diamond, either filled or in outline as specified by the user. For instance, here are filled and outline diamonds for n = 5:

    *              *
   * *            * *
  * * *          *   *
 * * * *        *     *
* * * * *      *       *
 * * * *        *     *
  * * *          *   *
   * *            * *
    *              *
Note that there is a single space between asterisks in the filled version of the diamond.

Your task is to write a program that draws diamonds as described above.

puzzle source: http://programmingpraxis.com/2014/09/09/drawing-diamonds/a
"""


def draw_diamond(n, filled=False):
    m = n + (n-1)

    i = n
    j = n
    while j <= m:
        s, e = (i, j)
        if filled:
            r = range(i, j+1)
        else:
            r = [s, e]
        print ''.join([' ' if t not in r else '*' for t in range(1, e+1)])
        i -= 1
        j += 1

    i += 2
    j -= 2
    while j >= n:
        s, e = (i, j)
        if filled:
            r = range(i, j+1)
        else:
            r = [s, e]
        print ''.join([' ' if t not in r else '*' for t in range(1, e+1)])
        i += 1
        j -= 1

# But we could do it better...

def diamond_better(n, filled=False):
    def render_aux(n, i, filled):
        if filled:
            print ''.join([' '*(n-i), '* '*i])
        else:
            if i == 1:
                print ''.join([' '*(n-i), '*'])
            else:
                print ''.join([' '*(n-i), '*', ' '*(2*i-3), '*'])
    i = 1
    while i <= n:
        render_aux(n, i, filled)
        i += 1

    i = n - 1
    while i > 0:
        render_aux(n, i, filled)
        i -= 1
