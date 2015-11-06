from behave import *
import random

level_file = open("levels.txt", "w+")
try:
    current_level = int(level_file.read())
except ValueError:
    level_file.write("1")
    current_level = 1
level_file.close()

import usercode


@given("Level 1 is unlocked")
def step_impl(context):
    assert (current_level >= 1), "Level 1 is currently locked"
@when("Level 1 code is submitted")
def step_impl(context):
    assert (callable(getattr(usercode, "level_1", None))), "The function `level_1()` does not exist"
@then("the function `level_1()` should return `'Hello, world!'`")
def step_impl(context):
    assert (usercode.level_1() == "Hello, world!"), "The function `level_1()` did not return `'Hello, world!'`"
    level_file = open("levels.txt", "w")
    level_file.write("2")
    level_file.close()

@given("Level 2 is unlocked")
def step_impl(context):
    assert (current_level >= 2), "Level 2 is currently locked"
@when("Level 2 code is submitted")
def step_impl(context):
    assert (callable(getattr(usercode, "level_2", None))), "The function `level_2()` does not exist"
@then("the function `level_2()` should return its input")
def step_impl(context):
    assert (usercode.level_2("This is a string") == "This is a string"), "The function `level_2()` did not return its input"
    level_file = open("levels.txt", "w")
    level_file.write("3")
    level_file.close()

@given("Level 3 is unlocked")
def step_impl(context):
    assert (current_level >= 3), "Level 3 is currently locked"
@when("Level 3 code is submitted")
def step_impl(context):
    assert (callable(getattr(usercode, "level_3", None))), "The function `level_3()` does not exist"
@then("the function `level_3()` should return its input plus `1`")
def step_impl(context):
    num = random.randint(-10, 10)
    assert (usercode.level_3(num) == num + 1), "The function `level_3()` did not return its input plus `1`"
    level_file = open("levels.txt", "w")
    level_file.write("4")
    level_file.close()

@given("Level 4 is unlocked")
def step_impl(context):
    assert (current_level >= 4), "Level 4 is currently locked"
@when("Level 4 code is submitted")
def step_impl(context):
    assert (callable(getattr(usercode, "level_4", None))), "The function `level_4()` does not exist"
@then("the function `level_4()` should return `True` if the input minus `3` is positive or `False` if the input minus `3` is `0` or negative")
def step_impl(context):
    num = random.randint(-10, 10)
    if num - 3 > 0:
        result = True
    else:
        result = False
    assert (usercode.level_4(num) == result), "The function `level_4()` did not return `True` if the input minus `3` is positive or `False` if the input minus `3` is `0` or negative"
    level_file = open("levels.txt", "w")
    level_file.write("5")
    level_file.close()
