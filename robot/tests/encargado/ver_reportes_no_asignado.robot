
Criterio de aceptación: El encargado verá en su vista una 
lista con todos los reportes no asignados con su información, 
también podrá hacer click en un botón para asignar un reporte específico a un desarrollador.


*** Settings ***
Library  SeleniumLibrary
Resource    ../../resources/Functionality.robot
Resource    prioridad.robot
Test Teardown  Close Browser

*** Variables ***
    
*** Test Cases ***
This is my first test case
    [Documentation]  Test for "encargado"
    [Tags]  Functional
    
    Open Browser  http://localhost:5173/Asignacion  Firefox
    Maximize Browser Window
    Sleep    1
    Select VerificarReportes
    Select Cambiar_producto_Asignacion
    Sleep    1
    Select VerificarReportes
    Sleep    1
    
    Reload Page

*** Keywords ***

Select VerificarReportes
    Element Should Be Visible   class=row-state-asignacion0   
    Sleep    1

Select Cambiar_producto_Reporte
    
    Click Button  id:dropdown-listaReportesEnc   
    Sleep    1.5
    Click Link   id:producto-1 
    Sleep    1
    Click Button  id:dropdown-listaReportesEnc 
    Sleep    1
    Click Link   id:producto-2
    Sleep    1
    Click Button  id:dropdown-listaReportesEnc 
    Sleep    1
    Click Link   id:producto-1
    Sleep    1 

Select Cambiar_producto_Asignacion
    
    Select From List By Value   id:producto_asignacion    1   
    Sleep    1.5
    Select From List By Value   id:producto_asignacion    2
    Sleep    1



