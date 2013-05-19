Feature: Automating my home

    Scenario: Waking up a computer we know about
        Given there is a computer named "testable"
        When we try to wake it up
        Then we get back a 200
        And we get informed it is awake

    Scenario: Trying to wake up a computer that doesn't exist
        Given there is no computer named "untestable"
        When we try to wake it up
        Then we get back a 404

    Scenario: Sounding an alarm
        Given someone named "joe" has an alarm
        When we tell it to start sounding
        Then we get back a 200
        And we get informed it is sounding

    Scenario: Trying to sound an alarm that doesn't exist
        Given someone named "john" has no alarm
        When we tell it to start sounding
        Then we get back a 404
