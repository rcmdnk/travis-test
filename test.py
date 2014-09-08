#!/usr/bin/env python

def func1():
    print 1

def func2():
    print 2

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == "1":
            func1()
        if sys.argv[1] == "2":
            func2()
