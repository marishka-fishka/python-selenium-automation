# Created by Mary at 10/26/2019
Feature: Test for amazon wholefoods selection
  # Enter feature description here

  Scenario: Test case to verify that every product on the amazon page has a text ‘Regular’ and a product name.
    Given Open Amazon wholefoods page
    Then Verify that every product has a text "Regular"
    And Verify a product name