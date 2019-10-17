# Created by Mary at 10/12/2019
Feature: Cancelling an order on Amazon

  Scenario:Logged out user sees Cancel Orders page when clicking Cancel order on the Help page
    Given Open Amazon page and Amazon Help tab
    When Click on search field
    And Input cancel order in search field
    When Click on search icon1
    Then Search results for Cancel order is shown