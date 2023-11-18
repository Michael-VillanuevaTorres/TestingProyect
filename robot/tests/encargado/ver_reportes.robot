Criterio de aceptación: El encargado podrá ir a la página de un reporte, por medio de cualquier vista
haciendo click en el título de un reporte y realizar un comentario. 

*** Settings ***
Library  SeleniumLibrary
Resource    ../../resources/Functionality.robot
Test Teardown  Close Browser

*** Variables ***
    
*** Test Cases ***
This is my first test case
    [Documentation]  Test for "encargado"
    [Tags]  Functional
    # Given: El encargado esta en su vista principal y va a la pagina de todos los reportes
    Open Browser  http://localhost:5173/Asignacion  Firefox
    Maximize Browser Window
    Sleep    1
    Select MisReportes
    Sleep    1
    # When: Se buscar un reporte
    Select Cambiar_producto
    Select Buscar_reporte   
    Sleep    1
    # When: El encargado podra hacer click en el reporte
    Select VerReporte
    Sleep    1
    # Then: El encargado podra ver el reporte seleccionado y realizar un comentario
    Select VerificarReporte1
    
    Select Conmentario
    Sleep    1
    # When: El encargado va a su vista principal
    Select Asignacion
    Sleep    1
    # When: El encargado podra hacer click en el reporte
    Select VerReporte
    Sleep    1
    # Then: El encargado podra ver el reporte seleccionado
    Select VerificarReporte1

    Reload Page

*** Keywords ***

Select VerReporte
    Click Link    id:reporte-1
    Sleep    1

Select VerificarReporte1
    Element Should Be Visible   id:verReporte1
    Sleep    1

Select Buscar_reporte
    Input Text   id:search-listaReportesEnc    default_report
    Sleep    1
Select MisReportes
    
    Click Link    id:todos_reportes_bar
    Sleep    1

Select Asignacion
    
    Click Link    id:asignacion_bar
    Sleep    1

Select Cambiar_producto
    
    Click Button   id:dropdown-listaReportesEnc   
    Sleep    1
    Click Link   id:producto-1 
    Sleep    1
    Click Button  id:dropdown-listaReportesEnc
    Sleep    1
    Click Link   id:producto-2
    Sleep    1
    Click Button  id:dropdown-listaReportesEnc
    Sleep    1
    Click Link   id:producto-1


Select Conmentario
    
    Input Text    id:comentarios    Primer comentario
    Sleep    1
    Sleep    1
    Click Button    id:submit
    Sleep    1
    Sleep    1

