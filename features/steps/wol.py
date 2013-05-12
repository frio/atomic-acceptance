from behave import *
import requests

HOST = 'localhost:5000'


@given('there is a computer named "{hostname}"')
def impl(context, hostname):
    context.hostname = hostname


@when('we try to wake it up')
def impl(context):
    context.response = requests.put(
        'http://{0}/computer/{1}/'.format(HOST, context.hostname),
        data={'isAwake': True})


@then('we get back a 200')
def impl(context):
    assert context.response.status_code == 200


@then('we get back a JSON representation of its current state')
def impl(context):
    assert context.response.json() == {'isAwake': True}
