*** Settings ***
Library  SeleniumLibrary
Resource  ../../resources/base.robot


Test Teardown  base.Finish Test
*** Variables ***
${report_id}  3
*** Test Cases ***
Change The State Of A Report
    [Documentation]  Go to the view report page and change the state of a report
    Given a developer
    When he go to a report view a change the state of a report
    Then the state of the report is changed

*** Keywords ***

Given a developer
    base.INIT APP
    Sleep  1

When he go to a report view a change the state of a report
    Click Link  id:link-3
    Sleep  1
    Select From List By Index  id:select-priority  1
    Sleep  1

Then the state of the report is changed
    Go Back
    Sleep  1
    
