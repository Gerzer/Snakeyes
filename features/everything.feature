Feature: Snakeyes
  Scenario: Level 1
    Given Level 1 is unlocked
    When Level 1 code is submitted
    Then the function `level_1()` should return `'Hello, world!'`
  Scenario: Level 2
    Given Level 2 is unlocked
    When Level 2 code is submitted
    Then the function `level_2()` should return its input
  Scenario: Level 3
    Given Level 3 is unlocked
    When Level 3 code is submitted
    Then the function `level_3()` should return its input plus `1`
  Scenario: Level 4
    Given Level 4 is unlocked
    When Level 4 code is submitted
    Then the function `level_4()` should return `True` if the input minus `3` is positive or `False` if the input minus `3` is `0` or negative
