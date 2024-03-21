Feature: Test the search functionality of Secret Garden website

  @test1  @cookies
  Scenario: I can accept the cookies
    Given I am on the https://secretgarden.ro/
    When I click Accept Cookies button
    Then The cookies banner is not dislpayed anymore

  @test2
  Scenario Outline: Check if I can search a product in the search bar
    Given I am on the https://secretgarden.ro/
    When I search for "<product_name>" from search bar
    And I click the search button
    Then I have at least "<results_number>" results returned
    Examples:
      | product_name | results_number |
      | philodendron |      200       |
      | iasomie      |      40        |
      | ceramica     |      150       |
      | clematis     |      30        |


  @test3
  Scenario: Check if I can add a product into my shopping cart
    When I click the first product shown to the results page
    And I am redirected to the product's page
    And I click the "Adauga in cos" button
    And A sidebar with my shopping cart shows up
    Then The product should be found in my shopping cart


  @test4
  Scenario: Verify if I can remove a product from my shopping cart
    Given I am on the https://secretgarden.ro/
    When I click the shopping cart button from the homepage
    And A sidebar with my shopping cart shows up
    And I click the delete icon of the product
    Then The shopping cart is empty

  @test5
  Scenario Outline: Verify sorting by price filter
    Given I am on the https://secretgarden.ro/
    When I search for "<product>"
    And I sort the prices from low to high
    Then The prices should be sorted correctly
    Examples:
      |product  |
      |Haworthia|

  @test6
  Scenario: Check if I can select an option from the "Oferta Produs" menu
    Given I am on the https://secretgarden.ro/
    When I hover over the menu and I click the first option
    Then I am redirected to https://secretgarden.ro/collections/bulbi-rizomi

