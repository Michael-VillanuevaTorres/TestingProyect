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
    
    
    Select Cambiar_producto
    Select Prioridad
    Select Asignacion
    Reload Page
    
*** Keywords ***

Select Cambiar_producto
    
    Select From List By Value   id:producto_asignacion    1   
    Sleep    1.5
    Select From List By Value   id:producto_asignacion    2
    Sleep    1

Select Prioridad
    
    Click Button    id:dropdown-prioridad
    Sleep    1
    Click Link    class:dropdown-item
    Sleep    1
    Sleep    1

Select Conmentario
    
    Click Button    id:asignacion-button
    Sleep    1
    Select From List By Label    name:developer  default_developer
    Sleep    1
    Click Button    id:enviar-asignacion
    Sleep    1
    Reload Page
    Sleep    1

Select Asignacion
    
    Click Button    id:asignacion-button
    Sleep    1
    Select From List By Label    name:developer  default_developer
    Sleep    1
    Click Button    id:enviar-asignacion
    Sleep    1
    Reload Page
    Sleep    1