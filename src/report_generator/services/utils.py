from collections.abc import Callable
from functools import partial


def inject_dependency(dependency_name: str, dependency_provider: Callable):
    """
    Injects a dependency into a function as a keyword argument.
    All non dependency arguments should be passed before the dependency.


    Args:
        dependency_name (str): name of the dependency
        dependency_provider (Callable): function that returns the dependency

    Returns:
        Callable: decorator that injects the dependency
    """

    assert callable(dependency_provider), 'dependency_provider not callable'

    def decorator(func):
        return partial(func, **{dependency_name: dependency_provider()})

    return decorator
