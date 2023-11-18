
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
    # Given: El encargado esta en su vista principal y puede ver la tabla asignacion
    Open Browser  http://localhost:5173/Asignacion  Firefox
    Maximize Browser Window
    Select Cambiar_producto_Asignacion
    # When : Se asigna un reporte a un desarollador
    Sleep    1
    Select Asignacion
    # Then: Se agrega el producto a el desarollador y se elimina de la tabla de asignacion
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
    Sleep    2
    Select VerificarAsignacion
    Sleep    1

Select VerificarAsignacion
    Mouse Down  id:row-developer1
    Element Should Contain  class:num_reportes1   1 (1)


Select Cambiar_producto_Asignacion
    
    Select From List By Value   id:producto_asignacion    1   
    Sleep    1.5
    Select From List By Value   id:producto_asignacion    2
    Sleep    1
    Select From List By Value   id:producto_asignacion    1 

