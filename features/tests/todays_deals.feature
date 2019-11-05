# Created by Mary at 10/29/2019
Feature: Test Scenarios for Today's deals functionality

   Scenario: User can open and close Today's deals under $25
      Given Open Amazon page
      When Store original windows
       And Click to open Deals under 25
       And Switch to the newly opened window
      Then Shop all deals are shown
      When Put item in the cart
      Then User can close new window and switch back to original
      When Refresh the page
      Then Verify cart has 1 item
