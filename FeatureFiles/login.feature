Feature: Transfer Funds
  As a customer
  I want to transfer funds
  So that I can manage my accounts

  Scenario: User is able to transfer funds successfully with different accounts
    Given I am on the testfire login page
    When I enter valid credentials and click on login
    Then I should be on the home page
    When I click on the transfer funds link
    Then I should be on the transfer funds page
    When I select a different account in the "From" field
    And I select a different account in the "To" field
    And I enter a valid amount to transfer
    And I click on the transfer button
    Then I should see a success message confirming the transfer

  Scenario: System throws an error when same account is selected in "To" and "From" fields
    Given I am on the testfire login page
    When I enter valid credentials and click on login
    Then I should be on the home page
    When I click on the transfer funds link
    Then I should be on the transfer funds page
    When I select the same account in the "From" and "To" fields
    And I enter a valid amount to transfer
    And I click on the transfer button
    Then I should see an error message indicating that the same account cannot be selected for transfer