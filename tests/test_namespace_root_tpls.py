""" namespace_root_tpls unit tests. """

from aedev.namespace_root_tpls.__init__ import __doc__, __version__


def test_docstring():
    """ test existence of this package project docstring. """
    assert __doc__
    assert isinstance(__doc__, str)


def test_version():
    """ test existence of this package project version number. """
    assert __version__
    assert isinstance(__version__, str)
    assert __version__.count(".") == 2
