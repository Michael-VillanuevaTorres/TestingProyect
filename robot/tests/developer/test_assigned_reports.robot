*** Settings ***
Library  SeleniumLibrary
Resource  ../../resources/base.robot

Test Teardown  base.Finish Test

*** Variables ***
${DEVELOPER}  1
*** Test Cases ***
Check Assigned Reports
    [Documentation]  Check that all assigned reports to a developer are displayed
    Given a developer in the view "Mis reportes Asignados"
    When is logged
    Then it should displayed a list of all reports assigned to the developer
 
*** Keywords ***
Given a developer in the view "Mis reportes Asignados"
    base.Init App

When is logged
    Sleep  2s

Then it should displayed a list of all reports assigned to the developer
    Page Should Contain Element  id:dev-1
