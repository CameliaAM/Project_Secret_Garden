Feature: Verify that the login section on the Secret Garden website works properly and I can access my account

    Background:
      Given I am on https://secretgarden.ro/
      When I click the My Account button
      Then The Login section appears


    @negativeTesting  @T1
    Scenario: Check if the user can log in with invalid password
      When I enter my valid email
      And I enter my invalid password
      And I click the "Autentificare" login button
      Then I receive an error message

    @negativeTesting  @T2
    Scenario: Check if the user can log in with invalid email
      When I enter my invalid email
      And I enter my valid password
      And I click the "Autentificare" login button
      Then I receive an error message

    @T3
    Scenario: Verify that the forgot password link works properly
      When I click the "Ai uitat parola?" link
      And The "Reseteaza parola" section appears
      And I enter my email
      And I click the reset password button
      Then The "Ti-a fost trimis email cu link pentru resetarea parolei." message appears

    @positiveTesting @T4
    Scenario: Check if the user can log in with valid credentials
      When I enter my valid email
      And I enter my valid password
      And I click the "Autentificare" login button
      Then I am logged in my account

