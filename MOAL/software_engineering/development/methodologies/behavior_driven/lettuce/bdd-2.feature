Feature: Subtract two numbers
    In order to get the difference of two numbers
    As users of math utilities
    We'll implement basic math functions for re-use

    Background:
        Given I am using this utility function

    Scenario: Subtract 2 and 3
        Given I have the numbers "2" and "3" to subtracta
        When I compute the difference of "2" and "3"
        Then I should see the number "-1"
