Criterio de aceptación: El encargado de proyecto debe tener 
la capacidad de asignar niveles de prioridad a los reportes, 
esto a través de distintas vistas y con niveles de prioridad predeterminados
, proporcionando una indicación clara a los desarrolladores sobre qué tareas
deben priorizar en su trabajo.


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
    Sleep    1
    Select Cambiar_producto_Asignacion
    Select PrioridadBaja
    Select Cambiar_producto_Asignacion
    Select PrioridadAlta
    Select MisReportes
    Select Cambiar_producto_Reporte
    Sleep    1
    Select PrioridadBaja
    Sleep    1
    Select PrioridadAlta
    Reload Page
    Sleep    1
    Select VerReporte
    Select PrioridadBaja
    Sleep    1
    Select PrioridadAlta
    Select Conmentario

*** Keywords ***

Select VerReporte
    Click Link   id:reporte-1
    Sleep    1

Select MisReportes
    
    Click Link    id:todos_reportes_bar
    Sleep    1

Select Asignacion
    
    Click Link    id:asignacion_bar
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
    Select From List By Value   id:producto_asignacion    1 

Select PrioridadBaja
    
    Click Button    id:dropdown-prioridad-report1
    Sleep    1
    Click Link    id:Baja
    Sleep    1
    Sleep    1
    Reload Page
    Sleep    1
    Element Text Should Be  id:Baja1  BAJA  
    


Select PrioridadAlta
    
    Click Button    id:dropdown-prioridad-report1
    Sleep    1
    Click Link    id:Alta
    Sleep    1
    Sleep    1
    Reload Page
    Sleep    1
    Element Text Should Be  id:Alta1  ALTA

Select Conmentario
    
    Input Text    id:comentarios    Primer comentario
    Sleep    1
    Sleep    1
    Click Button    id:submit
    Sleep    1
    Sleep    1

