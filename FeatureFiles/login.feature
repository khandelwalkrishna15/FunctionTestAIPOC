Feature: Navigate to Add Employee page

  Scenario: Login to the application
    Given I am on the login page
    When I enter "Admin" as the username
    And I enter "admin123" as the password
    And I click on the login button
    Then I should be logged in successfully

  Scenario: Navigate to Add Employee page
    Given I am logged in to the application
    When I navigate to the PIM page
    And I click on the Add Employee button
    Then I should be on the Add Employee page

  Scenario: Enable Create Login Details Toggle button
    Given I am on the Add Employee page
    When I enable the Create Login Details toggle button
    Then the toggle button should be enabled