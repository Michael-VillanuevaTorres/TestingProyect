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
    base.INIT APP
    Click Link  id:dev-all-reports

When the developer clicks a filter by product
    Click Link  id:dev-all-reports
    Click Button  id:dropdown-button-dark
    Click Link  id:product-2

Then the table of all reports of the product are filtered
    Page Should Contain Element  class:product-2
    Page Should Not Contain Element  class:product-1