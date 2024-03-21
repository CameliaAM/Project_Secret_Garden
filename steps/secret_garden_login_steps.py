from behave import *


# Background

@given('I am on https://secretgarden.ro/')
def step_impl(context):
    context.secret_garden_login.open_home_page()


@when('I click the My Account button')
def step_impl(context):
    context.secret_garden_login.click_account_button()


@then('The Login section appears')
def step_impl(context):
    context.secret_garden_login.login_form_presence()


# Scenario: Check if the user can log in with invalid password

@when('I enter my valid email')
def step_impl(context):
    context.secret_garden_login.insert_valid_email()


@when('I enter my invalid password')
def step_impl(context):
    context.secret_garden_login.insert_invalid_password()


@when('I click the "Autentificare" login button')
def step_impl(context):
    context.secret_garden_login.login_button()


@then('I receive an error message')
def step_impl(context):
    context.secret_garden_login.login_failed()


# Scenario: Check if the user can log in with invalid email

@when('I enter my invalid email')
def step_impl(context):
    context.secret_garden_login.insert_invalid_email()


@when('I enter my valid password')
def step_impl(context):
    context.secret_garden_login.insert_valid_password()


# Scenario: Verify that the forgot password link works properly


@when('I click the "Ai uitat parola?" link')
def step_impl(context):
    context.secret_garden_login.forgot_password_link()


@when('The "Reseteaza parola" section appears')
def step_impl(context):
    context.secret_garden_login.reset_password_section()


@when('I enter my email')
def step_impl(context):
    context.secret_garden_login.forgot_password_email()


@when('I click the reset password button')
def step_impl(context):
    context.secret_garden_login.reset_password_button()


@then('The "{reset_message}" message appears')
def step_impl(context, reset_message):
    context.secret_garden_login.reset_password_message(reset_message)


# Scenario: Check if the user can log in with valid credentials

@then('I am logged in my account')
def step_impl(context):
    context.secret_garden_login.my_account_page()


