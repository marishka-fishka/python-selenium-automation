# Created by Mary at 11/11/2019
Feature:Test for product page

  Scenario:Size tooltip is shown upon hovering over Add to cart button
   Given Open Amazon product B074TBCSC8 page
    When Hover over Add To Cart button
    Then Verify size selection tooltip is shown

  Scenario:User sees the deals upon hovering over Sales and Deals
   Given Open Amazon product B074TBCSC8 page
    When Hover over Sales and Deals button
    Then Verify that deals are present


  Scenario:User can select Books department
   Given Open Amazon page
    When Select Home & Kitchen department
    And Search for wardrobe
    Then "wardrobe" department is selected



