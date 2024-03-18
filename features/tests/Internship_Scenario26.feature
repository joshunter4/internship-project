Feature: User can open product detail and see three options of visualization


  Scenario: Open first product detail and see “architecture”, “interior”
    Given Open the main page
    When Log in to the page
    When Click on “off plan” at the left side menu
    When Click on the first product
    Then Verify the two options of visualization are “architecture”, “interior”
    Then Verify the visualization options are clickable