*** Settings ***
Library  SeleniumLibrary
Resource  ../../resources/base.robot

Test Setup  base.INIT APP
Test Teardown  base.Finish Test
*** Test Cases ***
Reasign Report
    [Documentation]  Reasign a report to another developer 

    Sleep  1
    ${report_id}  Get Table Cell  id:dev-1  5  1
    
    Click Button  id:request-reassignment-button
    Input Text  id:reassign-reason  Maikol Chupalo
    Click Button  id:send-reason
    Sleep  1
    Page Should Not Contain Element  ${report_id}

