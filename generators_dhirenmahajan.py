# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 

@author: dhire
"""
#RQ1
class Cheer:
    """
    >>> UC = Cheer("Bearcats")
    >>> for c in UC:
    ...     print(c)
    ...
    Give me an B
    Give me an e
    Give me an a
    Give me an r
    Give me an c
    Give me an a
    Give me an t
    Give me an s
    """
    def __init__(self, s):
        self.s = s
        self.index = -1

    def __iter__(self):
        return Cheer(self.s)

    def __next__(self):
        self.index += 1
        if self.index == len(self.s):
            raise StopIteration
        return "Give me an " + self.s[self.index]


#RQ2
class Countdown:
    """
    An iterator that counts down from N to 0.
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in Countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """
    
    def __init__(self, num):
        self.count = num

    def __iter__(self):
        return Countdown(self.count)

    def __next__(self):
        if self.count < 0:
            raise StopIteration
        n = self.count
        self.count -= 1
        return n


##############
# Generators #
##############

def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    n = 1
    while True:
        yield n
        n += 1
# RQ3
def evens():
    """A generator function that yields the infinite sequence of all even natural
    numbers, starting at 1.

    >>> m = evens()
    
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    n = 2
    while True:
        yield n
        n += 2

#RQ4
def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    
    >>> list(s)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    yield from map(lambda x: x * k, s)

# RQ5
def countdown(n):
    """
    A generator that counts down from N to 0.
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    >>> for number in countdown(2):
    ...     print(number)
    ...
    2
    1
    0
    """
    i = n
    while i >= 0:
        yield i 
        i-=1


# RQ6
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    i = n
    while i >=1:
        if i ==1:
            yield 1
            return 1
        if i %2==0:
            yield i 
            i =i//2
        else:
            yield i 
            i = 3*i +1

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)