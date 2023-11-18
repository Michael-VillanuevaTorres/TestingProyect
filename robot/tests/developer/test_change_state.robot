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

*** Keywords ***

Given a developer
    base.INIT APP

When he go to a report view a change the state of a report
    Click Link  id:link-${report_id}
    Select From List By Index  id:select-priority  2
    Click Button

Then the state of the report is changed
