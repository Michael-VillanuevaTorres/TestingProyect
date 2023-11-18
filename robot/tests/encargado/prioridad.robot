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
    # Given: El encargado esta en su vista principal 
    Open Browser  http://localhost:5173/Asignacion  Firefox
    Maximize Browser Window
    # When : Se cambia la prioridad en la vista principal
    Sleep    1
    Select Cambiar_producto_Asignacion
    Select PrioridadBaja
    #Then: Se cambia la prioridad
    Sleep    1
    Select VerificarPrioridadBaja
    Sleep    1

    # Given : Se va a la vista de todos los reportes
    Select MisReportes
    # When : Se cambia la prioridad en la vista de todos los reportes
    Select Cambiar_producto_Reporte
    Sleep    1
    Select PrioridadAlta
    #Then: Se cambia la prioridad
    Sleep    1.5
    Select VerificarPrioridadAlta
    
    # Given : Se va a la vista del reporte
    Select VerReporte
    # When : Se cambia la prioridad en la vista del reporte
    Select PrioridadBaja
    Sleep    1
    #Then: Se cambia la prioridad
    Select VerificarPrioridadBaja
    Sleep    1
    

*** Keywords ***

Select VerificarPrioridadAlta
    Element Should Be Visible   id:Alta1   
    Element Should Not Be Visible   id:No-asignado1  
    Element Should Not Be Visible   id:Baja1  
    Element Should Not Be Visible   id:Media1  

Select VerificarPrioridadBaja
    Element Should Be Visible    id:Baja1  
    Element Should Not Be Visible   id:No-asignado1  
    Element Should Not Be Visible   id:Alta1  
    Element Should Not Be Visible   id:Media1  
     



Select VerReporte
    Click Link   id:reporte-1
    Sleep    1

Select MisReportes
    
    Click Link    id:todos_reportes_bar
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



