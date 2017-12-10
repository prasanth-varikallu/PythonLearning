# This file contains the implementations of the examples from the
# website http://www.informit.com/articles/article.aspx?p=2320938


def my_coroutine():
    while True:
        val = yield
        print("Received ", val)


it = my_coroutine()
next(it)  # initialize it
it.send(5)
it.send('a')