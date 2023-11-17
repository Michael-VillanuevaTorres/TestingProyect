*** Settings ***
Library  SeleniumLibrary

*** Keywords ***
INIT APP
    Open Browser  http://localhost:5173/dev  ${BROWSER}
    Maximize Browser Window

Finish Test
    Close Browser