from behave import *


# Scenario : I can accept the cookies

@given('I am on the https://secretgarden.ro/')
def step_impl(context):
    context.secret_garden_search.open_homepage()


@when('I click Accept Cookies button')
def step_impl(context):
    context.secret_garden_search.accept_cookies()


@then('The cookies banner is not dislpayed anymore')
def step_impl(context):
    context.secret_garden_search.cookies_banner_is_not_displayed()


# Scenario : Check if I can search a product in the search bar


@when('I search for "{product_name}" from search bar')
def step_impl(context, product_name):
    context.secret_garden_search.insert_search_product(product_name)


@when('I click the search button')
def step_impl(context):
    context.secret_garden_search.click_search_button()


@then('I have at least "{results_number}" results returned')
def step_impl(context, results_number):
    context.secret_garden_search.check_search_results(results_number)


# Scenario : Check if I can add a product in my shopping cart

@when('I click the first product shown to the results page')
def step_impl(context):
    context.secret_garden_search.click_first_product()


@when("I am redirected to the product's page")
def step_impl(context):
    context.secret_garden_search.product_page()


@when('I click the "Adauga in cos" button')
def step_impl(context):
    context.secret_garden_search.click_add_to_cart_button()


@when('A sidebar with my shopping cart shows up')
def step_impl(context):
    context.secret_garden_search.shopping_cart_sidebar()


@then('The product should be found in my shopping cart')
def step_impl(context):
    context.secret_garden_search.product_should_be_found_in_cart()


# Scenario : Verify if I can remove a product from my shopping cart

@when('I click the shopping cart button from the homepage')
def step_impl(context):
    context.secret_garden_search.homepage_cart_button()


@when('I click the delete icon of the product')
def step_impl(context):
    context.secret_garden_search.remove_product_from_cart_button()


@then('The shopping cart is empty')
def step_impl(context):
    context.secret_garden_search.empty_shopping_cart()


# Scenario: Verify sorting by price filter
@when('I search for "Haworthia"')
def step_impl(context):
    context.secret_garden_search.search_haworthia()


@when('I sort the prices from low to high')
def step_impl(context):
    context.secret_garden_search.sort_prices_from_low_to_high()


@then('The prices should be sorted correctly')
def step_impl(context):
    context.secret_garden_search.verify_sorted_prices()


# Scenario: Check if I can select an option from the "Oferta Produs" menu

@when('I hover over the menu and I click the first option')
def step_impl(context):
    context.secret_garden_search.products_menu()


@then('I am redirected to https://secretgarden.ro/collections/bulbi-rizomi')
def step_impl(context):
    context.secret_garden_search.option1_page()
