Feature: Add two numbers
    In order to get the sum of two numbers
    As users of math utilities
    We'll implement basic math functions for re-use

    Background:
        Given I am using this utility function

    Scenario: Sum 2 and 3
        Given I have the numbers "2" and "3" to add
        When I compute its sum of "2" and "3"
        Then I should see the number "5"
