Feature: CardRepository.add_card

Scenario: Empty
    Given there is an empty repository
    When a card is added
    Then there is 1 cards in the repository

Scenario: Already exists
    Given there is an non-empty repository
    When a card is added with duplicate RFID
    Then an error is thrown


