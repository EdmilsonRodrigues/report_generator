from random import randint

from report_generator.services import utils


def test_inject_dependency():
    SOME_DEPENDENCY = 5

    @utils.inject_dependency('some_dependency', lambda: SOME_DEPENDENCY)
    def example_func_with_dependency(argument, some_dependency):
        return some_dependency + argument

    for _ in range(100):
        random_argument = randint(0, 100)
        expected = SOME_DEPENDENCY + random_argument

        result_1 = example_func_with_dependency(random_argument)

        assert result_1 == expected
