Feature: Swag Labs
  Scenario: 1 Successful Login
    Given I am on the Demo Login Page
    When I fill the account information for account StandardUser into the Username field and the Password field
    And I click the Login Button
    Then I am redirected to the Demo Main Page
    And I verify the App Logo exists

  Scenario: 2 Failed Login
    Given I am on the Demo Login Page of scenario2
    When I fill the account information for account LockedOutUser into the Username field and the Password field
    And I click the Login Button of scenario2
    Then I verify the Error Message contains the text "Sorry, this user has been banned. "
