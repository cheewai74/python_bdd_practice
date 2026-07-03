from behave import given, when, then
from calculator import add

@given(u'Calculator app runs')
def step_impl(context):
    print(u'Step: Given Calculator app is running')

@when(u'I input \'{num1:d}\' and \'{num2:d}\'')
def step_impl(context, num1, num2):
    # Store the numbers and calculate the result (e.g., num1 - num2)
    context.num1 = num1
    context.num2 = num2
    context.result = num1 + num2  # or whatever your underlying function is

@then(u'I get result \'{expected_result:d}\'')
def step_impl(context, expected_result):
    # Assert that our calculated result matches the feature file expectation
    assert context.result == expected_result, f"Expected {expected_result}, but got {context.result}"