*** Settings ***
Library  SeleniumLibrary
Resource  ../../resources/base.robot

Test Setup  INIT APP
Test Teardown  Finish Test
*** Variables ***
${BROWSER}  firefox
*** Test Cases ***
Check All Reports
    [Documentation]  Check all reports of a product are displayed in the view of the link "Todos los reportes"
    [Tags]  Functional

    Click Link  id:dev-all-reports
    Click Button  id:dropdown-button-dark
    Click Link  id:product-1
    Element Text Should Be  class:row-id-product  1
    Element Text Should Not Be  class:row-id-product  2
    
*** Keywords ***
INIT APP
    Open Browser  http://localhost:5173/dev  ${BROWSER}
    Maximize Browser Window

Finish Test
    Close Browser
