Feature: CardRepository.add_card

Scenario: Empty
    Given there is an empty repository
    When a card is added
    Then there is 1 cards in the repository


