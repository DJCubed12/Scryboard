Feature: Creation operations for CardRepository

Scenario: Empty
    Given there is an empty repository
    When a card is added
    Then there is 1 cards in the repository

Scenario: Already exists
    Given there is an non-empty repository
    When a card is added with duplicate RFID
    Then an error is thrown

Scenario: Add to Library
    Given there is an non-empty repository
    When a card is added with zone L
    Then the card has zone L
    And the card is face down

Scenario: Add to Battlefield
    Given there is an non-empty repository
    When a card is added with zone B
    Then the card has zone B
    And the card is face up

Scenario: Add to Exile
    Given there is an non-empty repository
    When a card is added with zone E
    Then the card has zone E
    And the card is face up

Scenario: Add to Graveyard
    Given there is an non-empty repository
    When a card is added with zone G
    Then the card has zone G
    And the card is face up

Scenario: Add to Command
    Given there is an non-empty repository
    When a card is added with zone C
    Then the card has zone C
    And the card is face up

Scenario: Add to NOT_PRESENT
    Given there is an non-empty repository
    When a card is added with zone N
    Then the card has zone N
    And the card is face up


