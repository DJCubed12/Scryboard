Feature: Update operations for CardRepository

Scenario: Set Zone L
    Given there is an non-empty repository
    When I select a card
    And set its zone to L
    Then the card has zone L
    And the card is face down
Scenario: Set Zone B
    Given there is an non-empty repository
    When I select a card
    And set its zone to B
    Then the card has zone B
    And the card is face up
Scenario: Set Zone C
    Given there is an non-empty repository
    When I select a card
    And set its zone to C
    Then the card has zone C
    And the card is face up
Scenario: Set Zone G
    Given there is an non-empty repository
    When I select a card
    And set its zone to G
    Then the card has zone G
    And the card is face up
Scenario: Set Zone E
    Given there is an non-empty repository
    When I select a card
    And set its zone to E
    Then the card has zone E
    And the card is face up
Scenario: Set Zone N
    Given there is an non-empty repository
    When I select a card
    And set its zone to N
    Then the card has zone N
    And the card is face up

Scenario: Set API Id
    Given there is an non-empty repository
    When I select a card
    And set its API ID
    Then the card has the given API ID

Scenario: Flip card up
    Given there is an non-empty repository
    When I select a card
    And I flip the card face up
    Then the card is face up

Scenario: Flip card down
    Given there is an non-empty repository
    When I select a card
    And I flip the card face down
    Then the card is face down

Scenario: Set front image
    Given there is an non-empty repository
    When I select a card
    And I set the front image
    Then the card's front image is set
    But the card's back image is not set
Scenario: Set back image
    Given there is an non-empty repository
    When I select a card
    And I set the back image
    Then the card's back image is set
    But the card's front image is not set
Scenario: Set front and back image
    Given there is an non-empty repository
    When I select a card
    And I set both images
    Then the card's front image is set
    And the card's back image is set


