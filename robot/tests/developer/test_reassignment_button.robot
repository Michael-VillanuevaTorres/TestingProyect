*** Settings ***
Library  SeleniumLibrary
Resource  ../../resources/base.robot


Test Teardown  base.Finish Test
*** Variables ***
${report_id}  3

*** Test Cases ***
Reasign Report
    [Documentation]  Reasign a report to another developer 
    
    GIVEN a developer with a report
    WHEN he want to reasign the report
    Then open a request for reasignment

*** Keywords ***

Given a developer with a report
    base.INIT APP
When he want to reasign the report
    Click Button  id:request-${report_id}
    Input Text  id:reassign-reason  Input text test
    Click Button  id:send-reason
    Sleep  1
Then open a request for reasignment
    Page Should Not Contain Element  id:request-${report_id}

