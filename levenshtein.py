"""
In a previous exercise we computed the edit distance between two strings where
the allowable operations were insert or delete characters; we made the
calculation by determining the longest common subsequence. A different
definition of edit distance allows substitutions as well as insertions and
deletions, and is called the Levenshtein distance, since it was studied by
Vladimir Levenshtein in 1965. For example, the edit distance between “hill”
and “hilt” is 2 (delete the “l” and insert the “t”) but the
Levenshtein distance is 1 (replace “l” by “t”).

The basic algorithm is recursive: if either string is empty, the Levenshtein
distance is the length of the other string, otherwise it is the minimum of the
Levenshtein distance computed by deleting the first character from the first
string, by deleting the first character from the second string, or by deleting
the first characters of each of the two strings (adding 1 if the two characters
differ), plus the Levenshtein distance of the remaining substrings. That
computation takes exponential time as it recomputes the same substring
Levenshtein distances many times. A better algorithm uses dynamic programming
to build up the substring distances, so they are always available as
they are needed.

Your task is to write two functions to compute the Levenshtein distance
between two strings.
"""


def levenshtein_rec(s1, s2):
    pass


def make_matrix(n, m):
    return [[0 for i in range(m+1)] for j in range(n+1)]


def levenshtein_iter(s1, s2):
    n = len(s1)
    m = len(s2)
    d = make_matrix(n, m)

    if (n == 0):
        return m
    if (m == 0):
        return n

    for i in range(n+1):
        d[i][0] = i

    for j in range(m+1):
        d[0][j] = j

    for i in range(1, n+1):
        s1_i = s1[i-1]
        for j in range(1, m+1):
            s2_j = s2[j-1]
            if s1_i == s2_j:
                cost = 0
            else:
                cost = 1

            d[i][j] = min([d[i-1][j]+1, d[i][j-1]+1, d[i-1][j-1] + cost])

    return d[n][m]
