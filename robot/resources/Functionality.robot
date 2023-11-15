
*** Settings ***

Library  SeleniumLibrary

*** Keywords ***

Start TestEncargado
    Open Browser  http://localhost:5173/Asignacion  Firefox
    Maximize Browser Window

Finish Test
    Close Browser
