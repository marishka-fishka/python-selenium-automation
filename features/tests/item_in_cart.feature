# Created by Mary at 10/22/2019
Feature: Tests for cart icon functionality
  # Enter feature description here

  Scenario:User add item in the cart and verify number of items there
     Given Open Amazon page
     When Search for cartridge
     And Open the first product search result
     And Click Add to cart button
     And Close suggestion side section
    Then Verify cart has 1 item



