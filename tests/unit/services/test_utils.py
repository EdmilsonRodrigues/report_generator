from report_generator.services import utils


def test_inject_dependency(faker):
    SOME_DEPENDENCY = faker.pyint()

    @utils.inject_dependency('some_dependency', lambda: SOME_DEPENDENCY)
    def example_func_with_dependency(argument, some_dependency):
        return some_dependency + argument

    random_argument = faker.pyint()
    expected = SOME_DEPENDENCY + random_argument

    result_1 = example_func_with_dependency(random_argument)

    assert result_1 == expected
