import lettuce


@lettuce.step('I am using this utility function')
def sum_nums_start(step):
    pass


@lettuce.step('I have the numbers "([^"]*)" and "([^"]*)"')
def given_i_have_the_numbers_2_and_3_to_add(step, x, y):
    pass


@lettuce.step('I compute its sum of "([^"]*)" and "([^"]*)"')
def when_i_compute_its_sum(step, x, y):
    lettuce.world.result = int(x) + int(y)


@lettuce.step('I should see the number "([^"]+)"')
def then_i_should_see_the_number_5(step, expected):
    actual = lettuce.world.result
    assert int(actual) == int(expected)


# ------------------------------------------------------------------------------


@lettuce.step('I am using this utility function')
def subtract_nums_start(step):
    pass


@lettuce.step('I have the numbers "([^"]*)" and "([^"]*)"')
def given_i_have_the_numbers_2_and_3_to_subtract(step, x, y):
    pass


@lettuce.step('I compute the difference of "([^"]*)" and "([^"]*)"')
def when_i_compute_the_difference(step, x, y):
    lettuce.world.result = int(x) - int(y)


@lettuce.step('I should see the number "([^"]+)"')
def then_i_should_see_the_number_negative_one(step, expected):
    actual = lettuce.world.result
    assert int(actual) == int(expected)
