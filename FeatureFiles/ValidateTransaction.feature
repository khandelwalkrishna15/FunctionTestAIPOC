Feature: Transfer Funds
  As a customer
  I want to transfer funds from one account to another
  So that I can manage my finances effectively

  Scenario: User navigates to transfer funds page
    Given I am logged in to the testfire portal
    When I click on the "Transfer Funds" link
    Then I should be navigated to the transfer funds page

  Scenario Outline: User transfers funds successfully with different accounts
    Given I am on the transfer funds page
    When I select "<fromAccount>" in the "From" field
    And I select "<toAccount>" in the "To" field
    And I enter "<amount>" in the "Amount" field
    And I click on the "Transfer" button
    Then I should see a success message

    Examples:
      | fromAccount | toAccount | amount |
      | Account A   | Account B | 100    |
      | Account B   | Account C | 200    |

  Scenario: User receives an error when selecting the same account in "From" and "To" fields
    Given I am on the transfer funds page
    When I select the same account "<account>" in the "From" and "To" fields
    And I enter "<amount>" in the "Amount" field
    And I click on the "Transfer" button
    Then I should see an error message

    Examples:
      | account    | amount |
      | Account A  | 100    |
      | Account B  | 200    |