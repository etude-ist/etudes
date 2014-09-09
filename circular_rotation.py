"""
A string s is a circular rotation of a string t if it matches when the characters are circularly shifted by any number of positions; e.g., ACTGACG is 
a circular shift of TGACGAC, and vice versa. Detecting this condition is important in the study of genomic sequences. Write a program that checks whether 
two given strings s and t are circular shifts of one another.
"""


def circular_rotation(str_1, str_2):
    str_1_len = len(str_1)
    str_2_len = len(str_2)
    
    if str_1_len != str_2_len: return False
    
    i = 0
    j = 0
    while i < str_1_len:
        a = str_1[i]
        b = str_2[j]
        print (a, b)
        if a == b:
            i += 1
            j += 1
            if j == str_1_len:
                j = 0
        else:
            i = 0
            j += 1
            if j == str_1_len:
                return False
    return True


def test():
    assert circular_rotation('A', 'A') == True
    assert circular_rotation('A', 'B') == False
    assert circular_rotation('ACTGACG', 'TGACGAC') == True
    assert circular_rotation('TGACGAC', 'ACTGACG') == True
    assert circular_rotation('TGACGAC', 'TGACGAC') == True
    assert circular_rotation('ABABABAB', 'BABABABA') == True
    assert circular_rotation('ABABBBAB', 'BABABABA') == False
    assert circular_rotation('ACTGACG', 'ACTAACG') == False
    assert circular_rotation('ACTGACGFGH', 'CGFGHACTGA') == True
    assert circular_rotation('HCTGACGFGA', 'CGFGHACTGA') == False
    print 'all tests pass but ...'
