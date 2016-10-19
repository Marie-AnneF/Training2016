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
    nums2 = []
    for item in nums:
        if len(nums2):
            if nums2[-1] != item:
                nums2.append(item)
        else: nums2.append(item)  
    return nums2
  
def linear_merge(list1, list2):
    merged=[]
    merged=sorted(list1+list2)
    return merged

    
def main():
    print 'remove_adjacent'
    test(remove_adjacent([1, 2, 2, 3]), [1, 2, 3])
    test(remove_adjacent([2, 2, 3, 3, 3]), [2, 3])
    test(remove_adjacent([]), [])
    print
    print 'linear_merge'
    test(linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'xx'], ['bb', 'cc', 'zz']),
        ['aa', 'bb', 'cc', 'xx', 'zz'])
    test(linear_merge(['aa', 'aa'], ['aa', 'bb', 'bb']),
        ['aa', 'aa', 'aa', 'bb', 'bb'])

main()

def donuts(count):
    if count >= 10 :
        s='Number of donuts: many'
    else: 
        s='Number of donuts: '+ str(count)
    return s
    
def both_ends(s):
    if len(s) <= 2 :
        s2=""
    else:
        s2= s[:2:]+ s[-2]+s[-1]
    return s2


def fix_start(s):
    s2 = s.replace(s[0],"*")
    s3= s2.replace("*",s[0],1)
    return s3

def mix_up(a, b):
    s2 = a.replace(a[0:2],b[0:2]) + ' ' + b.replace(b[0:2],a[0:2])
    return s2
    
    
def main():
    print 'donuts'
    # Each line calls donuts, compares its result to the expected for that call.
    test(donuts(4), 'Number of donuts: 4')
    test(donuts(9), 'Number of donuts: 9')
    test(donuts(10), 'Number of donuts: many')
    test(donuts(99), 'Number of donuts: many')

    print
    print 'both_ends'
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')

  
    
    print
    print 'fix_start'
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')

    print
    print 'mix_up'
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')

main()

def verbing(s):
    if len(s) >= 3:
        if "ing" in s[len(s)-3:len(s)]:
            return s+"ly"
        else:
            return s+"ing"
    else :
        return s

def main():
    print 'verbing'
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

main()

