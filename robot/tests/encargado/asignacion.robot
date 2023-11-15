*** Settings ***
Library  SeleniumLibrary
Resource    ../../resources/Functionality.robot
Test Teardown  Close Browser

*** Variables ***
    
*** Test Cases ***
This is my first test case
    [Documentation]  Test for "encargado"
    [Tags]  Functional
    
    Open Browser  http://localhost:5173/Asignacion  Firefox
    Maximize Browser Window

    Select Asignacion

    
*** Keywords ***

Click LeerBug
    
    Click Link    id:titulo_reasignacion
    Sleep    0.5
    Select Prioridad
    Select Conmentario
    Click Link    id:asignacion_bar

Select Prioridad2
    
    Select From List By Value    class:dropdown
    Sleep    0.5
    Click Link    value:alta
    Sleep    0.5
    Reload Page
    Sleep    0.5

Select Prioridad
    
    Click Button    class:dropdown
    Sleep    0.5
    Click Link    value:alta
    Sleep    0.5
    Reload Page
    Sleep    0.5

Select Conmentario
    
    Click Button    id:asignacion-button
    Sleep    0.5
    Select From List By Label    name:developer  default_developer
    Sleep    0.5
    Click Button    id:enviar-asignacion
    Sleep    0.5
    Reload Page
    Sleep    0.5

Select Asignacion
    
    Click Button    id:asignacion-button
    Sleep    0.5
    Select From List By Label    name:developer  default_developer
    Sleep    0.5
    Click Button    id:enviar-asignacion
    Sleep    0.5
    Reload Page
    Sleep    0.5