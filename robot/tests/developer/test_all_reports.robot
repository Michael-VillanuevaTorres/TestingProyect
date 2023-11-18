*** Settings ***
Library  SeleniumLibrary
Resource  ../../resources/base.robot

Test Teardown  base.Finish Test
*** Test Cases ***    
Check All Report Of Product
    [Documentation]  Check all reports of a product are filtered in the view of the link "Todos los reportes"
    Given a developer in the view "Todos los reportes"
    When the developer clicks a filter by product
    Then the table of all reports of the product are filtered
    
*** Keywords ***
Given a developer in the view "Todos los reportes"
    base.Init App
    Click Link  id:dev-all-reports
    Sleep  1

When the developer clicks a filter by product
    Click Link  id:dev-all-reports
    Sleep  1
    Click Button  id:dropdown-button-dark
    Sleep  1
    Click Link  id:product-2

Then the table of all reports of the product are filtered
    Page Should Contain Element  class:product-2
    Page Should Not Contain Element  class:product-1