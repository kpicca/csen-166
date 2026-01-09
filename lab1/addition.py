# addition.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
Run python autograder.py
"""


def add(a, b):
    "Return the sum of a and b"
    "*** YOUR CODE HERE ***"
    return 0


# Local test
def unit_test():
    p1,p2=(11,2200.33)
    expected = p1+p2
    res = add(p1,p2)
    print(f"test::  {p1} + {p2} = {res} ",
          ("CORRECT" if res == expected else "FAILED [expected " + str(expected) + "]"))

if __name__ == '__main__':
    "This code runs when you invoke the script from the command line"
    unit_test()