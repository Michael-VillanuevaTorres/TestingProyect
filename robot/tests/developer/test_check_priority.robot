*** Settings ***
Library  SeleniumLibrary
Resource  ../../resources/base.robot


Test Teardown  base.Finish Test
*** Test Cases ***
Check a priority
    Given a developer
    When want to check a priority
    Then the priority should be checked

*** Keywords ***
Given a developer
    base.Init App
    Sleep  1

When want to check a priority
    Element Should Contain  id:report-3  MEDIA

Then the priority should be checked
    Sleep  1
