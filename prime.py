"""
prime.py -- Write the application code here
"""
import math
def main(x):

    liste = []

    if type(x) != int:
        return 'Must be int, please try again'

    elif x == 1:
        return []

    while x % 2 == 0:
        liste.append(2)
        x = x/2

    for i in range( 3, int(math.sqrt(x))+1, 2 ):
        while x % i == 0:
            liste.append(int(i))
            x = x/i

    if x > 2:
        liste.append(int(x))

    return liste


def test_1():
    assert main('x') == 'Must be int, please try again'
    #print(str(main('x')) + ' test 1 pass')

def test_2():
    assert main(1) == []
    #print(str(main(1)) + ' test 2 pass')

def test_3():
    assert main(2) == [2]
    #print(str(main(2)) + ' test 3 pass')

def test_4():
    assert main(3) == [3]
    #print(str(main(3)) + ' test 4 pass')

def test_5():
    assert main(4) == [2, 2]
    #print(str(main(4)) + ' test 5 pass')

def test_6():
    assert main(6) == [2, 3]
    #print(str(main(6)) + ' test 6 pass')

def test_7():
    assert main(8) == [2, 2, 2]
    #print(str(main(8)) + ' test 7 pass')

def test_8():
    assert main(9) == [3, 3]
    #print(str(main(9)) + ' test 8 pass')

#if __name__ == '__main__':
#    test_1()
#    test_2()
#    test_3()
#    test_4()
#    test_5()
#    test_6()
#    test_7()
#    test_8()
