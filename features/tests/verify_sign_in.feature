# Created by Mary at 10/12/2019
Feature: Tests for Orders functionality
  # Enter feature description here

  Scenario: Logged out user sees Sign in page when clicking Orders
    Given Open Amazon page
    When Click Amazon Orders link
    Then Verify Sign In page is opened