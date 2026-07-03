from behave import *

@given(u'I have behave installed')
def step_impl(context):
    pass

@when(u'I will proceed to implement test')  
def step_impl(context):
    assert True is not False

@then(u'behave will test it for us!')
def step_impl(context):
    assert context.failed is False