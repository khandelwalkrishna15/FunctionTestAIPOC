Feature: Transfer Funds
  As a customer
  I want to login to the testfire portal
  So that I can transfer funds successfully

  Background:
    Given the login details for the application are:
      | UserName | Password |
      | jsmith   | demo1234 |

  Scenario: User navigates to transfer fund page
    Given I am logged in to the testfire portal
    When I click on the transfer funds link
    Then I should be navigated to the transfer fund page

  Scenario: User transfers funds successfully with different accounts
    Given I am logged in to the testfire portal
    And I am on the transfer fund page
    When I select a different account in the "From" field
    And I select a different account in the "To" field
    And I enter the amount to transfer
    And I click on the transfer button
    Then the funds should be transferred successfully

  Scenario: System throws an error when same account is selected in "To" and "From" fields
    Given I am logged in to the testfire portal
    And I am on the transfer fund page
    When I select the same account in the "From" and "To" fields
    And I enter the amount to transfer
    And I click on the transfer button
    Then the system should throw an error message