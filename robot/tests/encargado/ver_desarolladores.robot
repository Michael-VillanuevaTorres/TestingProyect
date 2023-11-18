
Criterio de aceptación: El encargado verá la lista de desarrolladores asociados a un producto 
seleccionado y podrá ver la cantidad de reportes totales asignados a ese desarrollador y la 
cantidad de reportes asignados a ese producto, su nombre y un botón que le indicará más 
detalles de los reportes asignados al producto seleccionado.



*** Settings ***
Library  SeleniumLibrary
Resource    ../../resources/Functionality.robot
Test Teardown  Close Browser

*** Variables ***
    
*** Test Cases ***
This is my first test case
    [Documentation]  Test for "encargado"
    [Tags]  Functional
    # Given: El encargado esta en su vista principal y puede ver la tabla desarolaldores
    Open Browser  http://localhost:5173/Asignacion  Firefox
    Maximize Browser Window
    Sleep    1
    # When : Se selecciona el producto 1 la tabla desarolladores
    Select Cambiar_producto_Desarolladores_1
    Sleep    1
    # Then: Se ven los desarolaldores del producto seleccionado
    Select VerificarDesarolladores_producto_1
    Sleep    1
    # When : Se selecciona el producto 2 la tabla desarolladores
    Select Cambiar_producto_Desarolladores_2
    Sleep    1
    # Then: Se ven los desarolaldores del producto seleccionado
    Select VerificarDesarolladores_producto_2
    Sleep    1
    Select Reportes_del_desarollador_1
    
    Reload Page

*** Keywords ***

Select VerificarDesarolladores_producto_1
    Element Should Be Visible   class:producto_developer_1  
    Sleep    1
    Element Should Not Be Visible    class:producto_developer_2
    Sleep    1


Select VerificarDesarolladores_producto_2
    Element Should Be Visible   class:producto_developer_2
    Sleep    1
    Element Should Not Be Visible    class:producto_developer_1
    Sleep    1


Select Cambiar_producto_Desarolladores_1

    Select From List By Value   id:producto_desarolladores    1 
    Sleep    1.5
    

Select Cambiar_producto_Desarolladores_2
    
    Select From List By Value   id:producto_desarolladores    2 
    Sleep    1.5


Select Reportes_del_desarollador_1
    
    Click Button    id=developer1
    Sleep    1.5
    Sleep    1.5
