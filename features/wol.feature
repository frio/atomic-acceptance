Feature: Waking up a computer

    Scenario: Sending a RESTful request
        Given there is a computer named "testable"
        When we try to wake it up
        Then we get back a 200
        And we get back a JSON representation of its current state
