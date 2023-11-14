*** Settings ***
Library  SeleniumLibrary

*** Variables ***
    
*** Test Cases ***
This is my first test case
    [Documentation]  Google test
    [Tags]  regression

    Open Browser  https://www.google.com  firefox
    Close Browser
*** Keywords ***


