__author__ = 'Sukanya'

from .. paapa import A
from nose.tools import assert_equal
from nose.tools import assert_not_equal
from nose.tools import assert_raises
from nose.tools import raises

class TestA(object):
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass
    def setUp(self):
        pass

    def teardown(self):
        pass

    def test_init(self):
        a=A()
        assert_equal(a.value, "Some value", "Not equal");

    def test_asserttraise(self):
        a=A()
        assert_raises(KeyError, a.raise_exec,"A Value")