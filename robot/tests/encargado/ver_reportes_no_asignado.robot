
Criterio de aceptación: El encargado verá en su vista una 
lista con todos los reportes no asignados con su información, 
también podrá hacer click en un botón para asignar un reporte específico a un desarrollador.


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
    Sleep    1

    # When : Se selecciona un producto 1 en la tabla de asignacion
    Select Cambiar_producto_1
    Sleep    1
    # Then: Se ven los desarolaldores del producto seleccionado
    Select VerificarReportes_1
    Sleep    1
    # When : Se selecciona un producto 2 en la tabla de asignacio
    Select Cambiar_producto_2
    Sleep    1
    # Then: Se ven los desarolaldores del producto seleccionado
    Select VerificarReportes_2
    Sleep    1
    
    Reload Page

*** Keywords ***

Select VerificarReportes_1
    Element Should Be Visible      class:producto1 
    Element Should Not Be Visible    class:producto2
    Sleep    1

Select VerificarReportes_2
    Element Should Be Visible      class:producto2
    Element Should Not Be Visible    class:producto1
    Sleep    1

Select Cambiar_producto_1

    Select From List By Value   id:producto_asignacion    1 
    Sleep    1.5
    

Select Cambiar_producto_2
    
    Select From List By Value   id:producto_asignacion    2
    Sleep    1.5


