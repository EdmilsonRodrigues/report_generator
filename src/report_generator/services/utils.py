from collections.abc import Callable
from functools import partial
from typing import Any


def inject_dependency(
    dependency_name: str, dependency_provider: Callable[[], Any]
):
    """
    Injects a dependency into a function as a keyword argument.
    All non dependency arguments should be passed before the dependency.

    :param dependency_name: name of the dependency
    :type dependency_name: str
    :param dependency_provider: function that provides the dependency
    :type dependency_provider: Callable[[], Any]

    :return: decorator that injects the dependency
    :rtype: Callable[[Callable], Callable]
    """

    assert callable(dependency_provider), 'dependency_provider not callable'

    def decorator(func):
        return partial(func, **{dependency_name: dependency_provider()})

    return decorator
