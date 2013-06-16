from behave import *
import requests

HOST = 'localhost:5000'


@given('there is {} computer named "{hostname}"')
def impl(context, _, hostname):
    context.hostname = hostname


@when('we try to wake it up')
def impl(context):
    context.response = requests.put(
        'http://{0}/computer/{1}/'.format(HOST, context.hostname),
        data={'isAwake': True})


@then('we get back a {:d}')
def impl(context, expected_status):
    print(context.response.text)
    assert context.response.status_code == expected_status


@then('we get informed it {state} {stateType}')
def impl(context, state, stateType):
    expected_value = (state == "is")
    expected_key = "{}{}".format(state.capitalize(), stateType.capitalize())
    assert context.response.json()[expected_key] == expected_value


@given('someone named "{name}" has {dont_care} alarm')
def impl(context, name, dont_care):
    context.room_name = name

@when('we tell it to start sounding')
def impl(context):
    context.response = requests.put(
        'http://{0}/alarm/{1}/'.format(HOST, context.room_name),
        headers={'Content-Type': 'application/json'},
        data='{"IsSounding": true}')
