import logging


def test():
    return int("foo")


try:
    test()
except:
    logging.exception("catch a error")
