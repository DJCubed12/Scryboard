Feature: CardRepository.add_card

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
    Then the card is in the repository with zone L
    And the card is face down

Scenario: Add to Battlefield
    Given there is an non-empty repository
    When a card is added with zone B
    Then the card is in the repository with zone B
    And the card is face up

Scenario: Add to Exile
    Given there is an non-empty repository
    When a card is added with zone E
    Then the card is in the repository with zone E
    And the card is face up

Scenario: Add to Graveyard
    Given there is an non-empty repository
    When a card is added with zone G
    Then the card is in the repository with zone G
    And the card is face up

Scenario: Add to Command
    Given there is an non-empty repository
    When a card is added with zone C
    Then the card is in the repository with zone C
    And the card is face up

Scenario: Add to NOT_PRESENT
    Given there is an non-empty repository
    When a card is added with zone N
    Then the card is in the repository with zone N
    And the card is face up


