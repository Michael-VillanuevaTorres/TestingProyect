*** Settings ***
Library  SeleniumLibrary
*** Variables ***
${BROWSER}  firefox
*** Keywords ***
Init App
    Open Browser  http://localhost:5173/dev  ${BROWSER}
    Maximize Browser Window

Finish Test
    Close Browser