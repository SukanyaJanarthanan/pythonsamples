__author__ = 'Sukanya'

class A(object):
    def __init__(self):
        self.value = "Some value"

    def return_true(self):
        return True

    def raise_exec(self, val):
        raise KeyError(val)