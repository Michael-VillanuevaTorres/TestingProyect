

Criterio de aceptación: El encargado podrá reasignar un reporte por 
medio de un botón al ver los reportes asignados a un desarrollador


*** Settings ***
Library  SeleniumLibrary
Resource    ../../resources/Functionality.robot
Resource    asignacion.robot
Test Teardown  Close Browser

*** Variables ***
    
*** Test Cases ***
This is my first test case
    [Documentation]  Test for "encargado"
    [Tags]  Functional
    # Given: El encargado esta en su vista principal y puede ver la tabla desarolladores
    
    Open Browser  http://localhost:5173/Asignacion  Firefox
    Maximize Browser Window
    Sleep    1
    # When : Se ven todos los reportes asignados a un desarollador 
    Select ReportesAsignados
    Sleep    1
    # When : Se reasigna el reporte a otro desarollador
    Select Reasignacion
    Sleep    1
    # Then : En el numero de reportes de cada desarollador cambia y se refleja el traspaso de reporte
    Select VerificarReasignacion
    Reload Page    

*** Keywords ***

Select ReportesAsignados
    Mouse Down  id:row-developer1
    Click Button    id:Reportes_asignado_developer1
    Sleep    1
Select Reasignacion
    
    Click Button    id:asignacion-button1
    Sleep    1
    Select From List By Value    class:form-select  2
    Sleep    1
    Click Button    id:enviar-asignacion
    Sleep    2


Select VerificarReasignacion
    Mouse Down  class:num_reportes1
    Element Should Not Contain    class:num_reportes1   1 (1)
    Sleep    1
    Mouse Down  class:num_reportes2
    Element Should Contain    class:num_reportes2   1 (1)
    Sleep    1
    
