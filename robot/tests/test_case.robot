*** Settings ***
Library  SeleniumLibrary

*** Variables ***
    
*** Test Cases ***
This is my first test case
    [Documentation]  Google test
    [Tags]  regression

    Open Browser  http://localhost:5173/  Firefox
    
*** Keywords ***


