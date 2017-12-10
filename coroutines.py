# This file contains the implementations of the examples from the
# website http://www.informit.com/articles/article.aspx?p=2320938


def my_coroutine():
    while True:
        val = yield
        print("Received ", val)


def call_1st_coroutine():
    it = my_coroutine()
    next(it)  # initialize it
    it.send(5)
    it.send('a')


def minimum_finding_coroutine():
    val = yield
    while True:
        val2 = yield val
        val = min(val, val2)

def call_2nd_coroutine():
    it = minimum_finding_coroutine()
    next(it)
    print(it.send(5))
    print(it.send(2))
    print(it.send(8))

call_2nd_coroutine()
