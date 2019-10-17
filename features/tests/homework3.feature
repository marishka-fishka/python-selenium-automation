# Created by Mary at 10/17/2019
Feature: Check that shopping  cart on Amazon
  # Enter feature description here

  Scenario: User can open Shopping cart on Amazon and check if it is empty
    Given Open Amazon page
    When Click on the cart icon
    Then Verify that Shopping cart is empty