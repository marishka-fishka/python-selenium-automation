# Created by Mary at 10/17/2019
Feature: Tests for hamburger menu functionality
  # Enter feature description here

  Scenario: Amazon Music has 6 menu items
    Given Open Amazon page
    When Click on hamburger menu
    And Click on Amazon Music menu item
    Then 6 menu items are present