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
    
    Sleep    1
    Select MisReportes
    Sleep    1
    Select Cambiar_producto
    Select Buscar_reporte
    Select PrioridadBaja
    Sleep    1
    Select VerReporte
    Select PrioridadAlta
    Select Conmentario
    Reload Page

*** Keywords ***

Select VerReporte
    Click Link    id=e1
    Sleep    1
Select Buscar_reporte
    Input Text   custom-search-bar    e1
    Sleep    1
Select MisReportes
    
    Click Link    id:todos_reportes_bar
    Sleep    1

Select Asignacion
    
    Click Link    id:asignacion_bar
    Sleep    1

Select Cambiar_producto
    
    Click Button  id:dropdown-button-dark    
    Sleep    1.5
    Click Link   id:default_product  
    Sleep    1
    Click Button  id:dropdown-button-dark 
    Sleep    1
    Click Link   id:default_product2
    Sleep    1
    Click Button  id:dropdown-button-dark 
    Sleep    1
    Click Link   id:default_product

Select PrioridadBaja
    
    Click Button    id:dropdown-prioridad
    Sleep    1
    Click Link    id:Baja
    Sleep    1
    Sleep    1
    Reload Page

Select PrioridadAlta
    
    Click Button    id:dropdown-prioridad
    Sleep    1
    Click Link    id:Alta
    Sleep    1
    Sleep    1
    Reload Page

Select Conmentario
    
    Input Text    id:comentarios    Primer comentario
    Sleep    1
    Sleep    1
    Click Button    id:submit
    Sleep    1
    Sleep    1

