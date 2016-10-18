# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""
def match_ends (somewords) :
    result = 0
    for s in somewords:
        if len(s) > 1 and s[0]==s[-1]:
            #print(s[-1])
            result+=1
    return result

x = ["tot", "file", "aria", "ete"]
print match_ends(x)


def front_x(words):
    words_x=[]
    words_other=[]
    for s in words:
        if s[0]=='x' :
            words_x.append(s)
        else:
            words_other.append(s)
    words_tri_x = sorted(words_x)
    words_tri = sorted(words_other)
    return words_tri_x + words_tri
    
def sort_last(tuples):
    tuplesby2 = sorted(tuples, key=lambda tup:tup[1])
    return tuplesby2
    
def test(got, expected):
    prefix = 'OK' if got == expected else ' X'
    # !r prints a Python representation of the strings (complete with quotes)
    print ' {} got: {!r} expected: {!r}'.format(prefix, got, expected)

def main():
    print 'match_ends'
    test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
    test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
    test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)
    print
    print 'front_x'
    test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
        ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
    print
    print 'sort_last'
    test(sort_last([(1, 3), (3, 2), (2, 1)]),
         [(2, 1), (3, 2), (1, 3)])
    test(sort_last([(2, 3), (1, 2), (3, 1)]),
         [(3, 1), (1, 2), (2, 3)])
    test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)])

main()

def remove_adjacent(nums):
  return
  
def main():
    print 'remove_adjacent'
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])

main()

