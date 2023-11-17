
Criterio de aceptación: El encargado irá a la tabla de reportes no asignados
y pulsará el botón para asignar, asignado a un desarrollador y después se 
verá en la pantalla el cambio en la cantidad de reportes asignados a ese desarrollador.

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
    Select Cambiar_producto_Asignacion
    Sleep    1
    Select Asignacion
    Select Cambiar_producto_Asignacion
    Select VerificarAsignacion
    Reload Page
    
*** Keywords ***

Select Asignacion
    
    Click Button    id:asignacion-button1
    Sleep    1
    Select From List By Value    name:developer  1
    Sleep    1
    Click Button    id:enviar-asignacion
    Sleep    1
    Reload Page
    Sleep    1

Select VerificarAsignacion
    Mouse Down  class:row-developer1
    Element Should Contain  num_reportes1   1(1)
Select VerReporte
    Click Link   id:reporte-1
    Sleep    1

Select MisReportes
    
    Click Link    id:todos_reportes_bar
    Sleep    1

Select Cambiar_producto_1
    
    Click Button  id:dropdown-listaReportesEnc   
    Sleep    1.5
    Click Link   id:producto-1 
    Sleep    1
Select Cambiar_producto_2
    Click Button  id:dropdown-listaReportesEnc 
    Sleep    1.5
    Click Link   id:producto-2
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

