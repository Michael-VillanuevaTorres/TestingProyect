*** Settings ***
Library  SeleniumLibrary
Resource  ../../resources/base.robot

Test Setup  base.INIT APP
Test Teardown  base.Finish Test
*** Variables ***
${BROWSER}  firefox
*** Test Cases ***    
Check All Reports
    [Documentation]  Check all reports of a product are displayed in the view of the link "Todos los reportes"
    [Tags]  Functional

    Click Link  id:dev-all-reports
    Click Button  id:dropdown-button-dark
    Click Link  id:product-2
    Page Should Contain Element  class:product-2
    Page Should Not Contain Element  class:product-1
    
*** Keywords ***

